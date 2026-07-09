"""OAuth2 token acquisition + refresh for the Imweb OPEN API.

Imweb uses an OAuth2 ``authorizationCode`` flow. The MCP server does NOT drive
the interactive browser authorization (that is a one-time step documented in
``CONNECTORS.md``); it consumes an ``access_token`` and, when available, silently
refreshes it via ``grant_type=refresh_token`` against ``POST /oauth2/token``.

Token rotation: Imweb may or may not return a new ``refresh_token`` on refresh.
When a new one is supplied it replaces the stored value; otherwise the existing
refresh token is retained.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

import httpx

if TYPE_CHECKING:
    from ._base import ImwebConfig


class ImwebAuthError(RuntimeError):
    """Raised when token refresh fails."""


@dataclass
class TokenPair:
    access_token: str
    refresh_token: str


def refresh_access_token(config: "ImwebConfig", client: Optional[httpx.Client] = None) -> TokenPair:
    """Exchange ``refresh_token`` for a fresh ``access_token``.

    Uses the standard OAuth2 refresh-token grant (RFC 6749 §6) against the Imweb
    token endpoint. Credentials are sent as a form-encoded body (the Imweb docs
    accept ``client_id`` / ``client_secret`` in the body); Basic auth is layered
    on top as a harmless fallback for stricter deployments.
    """
    from ._base import DEFAULT_API_BASE  # noqa: F401  (kept for future base override)
    import base64

    if not config.can_refresh:
        raise ImwebAuthError(
            "토큰 갱신 불가 — IMWEB_CLIENT_ID / IMWEB_CLIENT_SECRET / IMWEB_REFRESH_TOKEN 중 누락. "
            "CONNECTORS.md 의 절차에 따라 토큰을 (재)발급 받아 .mcp.json env 에 설정하세요."
        )

    url = f"{config.api_base}/oauth2/token"
    # Imweb uses camelCase keys (matching its /oauth2/authorize params:
    # responseType, clientId, redirectUri, ...). Grant *values* stay OAuth2-standard.
    form = {
        "grantType": "refresh_token",
        "refreshToken": config.refresh_token,
        "clientId": config.client_id,
        "clientSecret": config.client_secret,
    }
    headers = {"Accept": "application/json"}
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
        # Tolerate both camelCase (Imweb convention) and snake_case (OAuth2 std) keys.
        new_access = data.get("accessToken") or data.get("access_token")
        if resp.status_code >= 400 or not new_access:
            raise ImwebAuthError(
                f"토큰 갱신 실패 (HTTP {resp.status_code}): {data}. "
                "refresh_token 이 만료되었을 수 있습니다 — CONNECTORS.md 재발급 절차 참고."
            )
        new_refresh = data.get("refreshToken") or data.get("refresh_token") or config.refresh_token
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
