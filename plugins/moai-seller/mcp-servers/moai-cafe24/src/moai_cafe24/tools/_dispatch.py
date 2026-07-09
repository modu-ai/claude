"""Compile registry endpoints into typed FastMCP tools at startup.

Each :class:`~moai_cafe24.registry.Endpoint` becomes one MCP tool:

  * path placeholders (``{product_no}``) → required ``str`` keyword args
  * declared ``query_params`` → optional typed keyword args
  * every tool → optional ``shop_no: int`` (merged into query or body)
  * body endpoints → optional ``body: dict`` (wrapped as ``{body_key: body}``)
  * list endpoints → optional ``paginate: bool`` / ``max_pages: int`` (transparent
    offset pagination via :meth:`Cafe24Client.list_paginated`)

The generated functions carry a real ``inspect.Signature`` + ``__annotations__``
so FastMCP/pydantic produce a precise JSON schema per tool — the MCP client sees
named, typed, documented parameters, not a generic blob.
"""

from __future__ import annotations

import inspect
from typing import Annotated, Any, Optional

from pydantic import Field

from .._app import mcp
from .._base import get_client
from ..client import SURFACE_ANALYTICS, Cafe24ApiError
from ..registry import REGISTRY, Endpoint, Param

_TYPE_MAP = {"str": str, "int": int, "float": float, "bool": bool}


def _param_annotation(p: Param):
    """Build the per-parameter type annotation with a structured description.

    FastMCP/pydantic lift ``Annotated[...]`` ``Field(description=...)`` into the
    tool JSON-schema per-property ``description`` (A5). The docstring ``Args:``
    section is kept as a human-readable parallel, but the structured channel the
    model reads at selection time is the Field description, so it is the source
    of truth here.
    """
    ann = _TYPE_MAP.get(p.type, str)
    desc = (p.description or "").strip() or None
    if p.required:
        return ann if desc is None else Annotated[ann, Field(description=desc)]
    # noqa: UP045 — Optional reads cleanly in tooling introspection
    return Optional[ann] if desc is None else Annotated[Optional[ann], Field(description=desc)]


def _param_default(p: Param):
    if p.required:
        return inspect.Parameter.empty
    return p.default if p.default is not None else None


def _build_signature(ep: Endpoint) -> inspect.Signature:
    params: list[inspect.Parameter] = []
    declared = set()
    # Path params first (required).
    for name in ep.path_param_names:
        declared.add(name)
        params.append(
            inspect.Parameter(
                name,
                inspect.Parameter.KEYWORD_ONLY,
                annotation=Annotated[str, Field(description=f"path parameter ({name})")],
            )
        )
    # Declared query params.
    for p in ep.query_params:
        declared.add(p.name)
        params.append(
            inspect.Parameter(
                p.name,
                inspect.Parameter.KEYWORD_ONLY,
                annotation=_param_annotation(p),
                default=_param_default(p),
            )
        )
    # Universal shop_no — only if not already a path/query param (e.g. shops/{shop_no}).
    if "shop_no" not in declared:
        params.append(
            inspect.Parameter(
                "shop_no",
                inspect.Parameter.KEYWORD_ONLY,
                annotation=Annotated[Optional[int], Field(description="multi-shop number (default per config)")],
                default=None,
            )
        )
    # Body.
    if ep.takes_body:
        bk = ep.resolved_body_key
        wrap = f"wrapped as {{\"{bk}\": ...}}" if bk else "sent as-is (raw)"
        params.append(
            inspect.Parameter(
                "body",
                inspect.Parameter.KEYWORD_ONLY,
                annotation=Annotated[Optional[dict], Field(description=f"request body fields, {wrap}")],
                default=None,
            )
        )
    # Pagination opt-in.
    if ep.list_endpoint:
        params.append(
            inspect.Parameter(
                "paginate",
                inspect.Parameter.KEYWORD_ONLY,
                annotation=Annotated[bool, Field(description="auto-follow offset pagination")],
                default=False,
            )
        )
        params.append(
            inspect.Parameter(
                "max_pages",
                inspect.Parameter.KEYWORD_ONLY,
                annotation=Annotated[int, Field(description="cap on pages when paginating")],
                default=50,
            )
        )
    return inspect.Signature(params)


def _build_docstring(ep: Endpoint) -> str:
    lines: list[str] = []
    lines.append(ep.summary or ep.name)
    if ep.description:
        lines.append("")
        lines.append(ep.description)
    lines.append("")
    scope = ep.scope or "(none)"
    lines.append(f"Scope: {scope}  |  Surface: {ep.surface}  |  {ep.method} {ep.path}")
    if ep.notes:
        lines.append(f"Notes: {ep.notes}")
    # Parameters — Google-style `Args:` so FastMCP/griffe lifts each entry into
    # the tool JSON-schema per-property `description` (A5: otherwise ~1869 params
    # across the catalog carry no structured-level description, degrading the
    # model's parameter selection). 4-space indent matches the Google convention.
    args: list[str] = []
    for name in ep.path_param_names:
        args.append(f"    {name} (str): path parameter (required).")
    for p in ep.query_params:
        desc = (p.description or "").strip()
        if p.required:
            args.append(f"    {p.name} ({p.type}): {desc} (required)")
        else:
            args.append(f"    {p.name} ({p.type}, optional): {desc}".rstrip())
    args.append("    shop_no (int, optional): multi-shop number (default per config).")
    if ep.takes_body:
        bk = ep.resolved_body_key
        wrap = f"wrapped as {{\"{bk}\": ...}}" if bk else "sent as-is (raw)"
        args.append(f"    body (dict, optional): request body fields, {wrap}.")
    if ep.list_endpoint:
        args.append("    paginate (bool, optional): auto-follow offset pagination (default False).")
        args.append("    max_pages (int, optional): cap on pages when paginating (default 50).")
    if args:
        lines.append("")
        lines.append("Args:")
        lines.extend(args)
    return "\n".join(lines)


def _tool_meta(ep: Endpoint) -> dict[str, Any]:
    """Build the per-tool ``_meta`` block declared in the tools/list response.

    list endpoints can return up to ``max_pages × page_size`` rows in a single
    response (default 50 × 100 = 5,000 rows), which routinely exceeds the MCP
    25K-token default output limit and is silently truncated to a file
    reference. Declare a raised ceiling so the host keeps the full result inline
    (A2). Per-call budget still applies; this only lifts the persist threshold.
    """
    if ep.list_endpoint:
        return {"anthropic/maxResultSizeChars": 200000}
    return {}


def _make_handler(ep: Endpoint):
    """Return a keyword-only closure that executes one endpoint call."""

    def handler(**kwargs: Any) -> Any:
        client = get_client()
        # Path params.
        path_params: dict[str, Any] = {}
        for name in ep.path_param_names:
            val = kwargs.pop(name, None)
            if val is None:
                raise Cafe24ApiError(0, "MISSING_PATH_PARAM", f"path parameter '{name}' is required", None, ep.path)
            path_params[name] = val
        # Query params (only declared ones).
        query: dict[str, Any] = {}
        for p in ep.query_params:
            if p.name in kwargs and kwargs[p.name] is not None:
                query[p.name] = kwargs.pop(p.name)
        # shop_no universal.
        shop_no = kwargs.pop("shop_no", None)
        # Pagination opt-in.
        paginate = bool(kwargs.pop("paginate", False)) if ep.list_endpoint else False
        max_pages = int(kwargs.pop("max_pages", 50)) if ep.list_endpoint else 50
        # Body.
        body = kwargs.pop("body", None) if ep.takes_body else None

        # Place shop_no per Cafe24 convention.
        if shop_no is not None:
            if ep.method.upper() in ("GET", "DELETE"):
                query["shop_no"] = shop_no
            else:
                body = dict(body or {})
                body.setdefault("shop_no", shop_no)

        # Analytics surface: mall_id is mandatory and config-derived — auto-inject.
        if ep.surface == SURFACE_ANALYTICS and not query.get("mall_id"):
            query["mall_id"] = client.config.mall_id

        # Wrap body.
        json_body: Any = None
        if ep.takes_body and body is not None:
            bk = ep.resolved_body_key
            json_body = {bk: body} if bk else body

        # Execute.
        if ep.list_endpoint and paginate:
            return client.list_paginated(
                ep.path,
                surface=ep.surface,
                params=query or None,
                max_pages=max_pages,
            )
        return client.request(
            ep.method,
            ep.path,
            surface=ep.surface,
            path_params=path_params or None,
            params=query or None,
            json_body=json_body,
        )

    sig = _build_signature(ep)
    handler.__signature__ = sig  # type: ignore[attr-defined]
    handler.__annotations__ = {p.name: p.annotation for p in sig.parameters.values()}
    handler.__name__ = ep.name
    handler.__doc__ = _build_docstring(ep)
    return handler


def register_all() -> int:
    """Register every endpoint in REGISTRY onto the shared FastMCP instance.

    Returns the number of tools registered. Idempotent guard prevents duplicate
    registration across re-imports.
    """
    count = 0
    for ep in REGISTRY.all():
        fn = _make_handler(ep)
        try:
            mcp.add_tool(fn, name=ep.name, description=fn.__doc__, meta=_tool_meta(ep))
        except Exception:
            # FastMCP raises if a tool name already exists; treat as already registered.
            continue
        count += 1
    return count
