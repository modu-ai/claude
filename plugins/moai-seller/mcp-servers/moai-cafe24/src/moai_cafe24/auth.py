"""OAuth2 token refresh for the Cafe24 API.

Cafe24 uses an OAuth2 ``authorization_code`` flow. The MCP server does NOT drive
the interactive browser authorization (a one-time step documented in
``README.md`` / ``CONNECTORS.md``); it consumes an ``access_token`` (2h TTL) and
silently refreshes it via ``grant_type=refresh_token`` against
``POST /api/v2/oauth/token``.

**Token rotation**: unlike some providers, Cafe24 **invalidates the prior
refresh token on every refresh** and returns a brand-new refresh token. The
caller MUST persist the new pair. See Cafe24 "Get Access Token using refresh
token": ``기존 refresh token은 만료처리되어 사용할 수 없습니다``.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

import httpx

if TYPE_CHECKING:
    from ._base import Cafe24Config


class Cafe24AuthError(RuntimeError):
    """Raised when token refresh fails."""


@dataclass
class TokenPair:
    access_token: str
    refresh_token: str


def refresh_access_token(config: "Cafe24Config", client: Optional[httpx.Client] = None) -> TokenPair:
    """Exchange ``refresh_token`` for a fresh ``access_token`` (+ rotated refresh).

    Posts the standard OAuth2 refresh-token grant (RFC 6749 §6) to the Cafe24
    token endpoint. Credentials are sent as a form-encoded body (Cafe24 docs
    show ``client_id`` / ``client_secret`` in the body); HTTP Basic is layered on
    top as a harmless fallback for stricter deployments.

    Returns the NEW token pair — both tokens must replace the stored values
    because the old refresh token is invalidated by Cafe24.
    """
    import base64

    if not config.can_refresh:
        raise Cafe24AuthError(
            "토큰 갱신 불가 — CAFE24_MALL_ID / CAFE24_CLIENT_ID / CAFE24_CLIENT_SECRET / "
            "CAFE24_REFRESH_TOKEN 중 누락. README.md 의 절차에 따라 토큰을 (재)발급 받아 "
            ".mcp.json env 에 설정하세요."
        )

    url = f"{config.admin_base}/api/v2/oauth/token"
    form = {
        "grant_type": "refresh_token",
        "refresh_token": config.refresh_token,
        "client_id": config.client_id,
        "client_secret": config.client_secret,
    }
    headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}
    # Layer HTTP Basic as well; servers that require it win, servers that ignore it pass.
    try:
        basic = base64.b64encode(f"{config.client_id}:{config.client_secret}".encode()).decode()
        headers["Authorization"] = f"Basic {basic}"
    except Exception:
        pass

    owns_client = client is None
    if owns_client:
        client = httpx.Client(timeout=config.timeout)
    try:
        resp = client.post(url, data=form, headers=headers)
        data = _safe_json(resp)
        if resp.status_code >= 400 or "access_token" not in data:
            raise Cafe24AuthError(
                f"토큰 갱신 실패 (HTTP {resp.status_code}): {data}. "
                "refresh_token 이 만료(2주)되었을 수 있습니다 — README.md 재발급 절차 참고."
            )
        new_access = data["access_token"]
        # Cafe24 rotates the refresh token; prefer the new one, fall back to the old
        # only if the server (unexpectedly) omits it.
        new_refresh = data.get("refresh_token") or config.refresh_token
        return TokenPair(access_token=new_access, refresh_token=new_refresh)
    finally:
        if owns_client:
            client.close()


def _safe_json(resp: httpx.Response) -> dict:
    try:
        if resp.headers.get("content-type", "").startswith("application/json"):
            return resp.json()
    except Exception:
        pass
    return {"_raw": resp.text}
