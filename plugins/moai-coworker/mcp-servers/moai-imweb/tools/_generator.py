#!/usr/bin/env python3
# (c) moai-imweb — OpenAPI → FastMCP category-dispatch tool generator.
# DO NOT EDIT the generated tools/*.py by hand; re-run this generator instead.
#
# Design (B안 — category dispatch): one MCP tool per OpenAPI tag.
#   imweb_<tag>(action: Literal[...], params=None, body=None, paginate=False)
# Each `action` is a snake_cased operation key unique within its tag; the tool
# resolves the (method, path, path-params, query-params, has-body) tuple from a
# generated `_OPS` table and delegates to ImwebClient.
#
# Source of truth: tools/openapi.json
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent  # mcp-servers/moai-imweb/tools/
ROOT = TOOLS_DIR.parent  # mcp-servers/moai-imweb/
SPEC_FILE = TOOLS_DIR / "openapi.json"
OUT_DIR = ROOT / "src" / "moai_imweb" / "tools"

# (OpenAPI tag, module slug, tool name, Korean label). Order = file emit order.
CATS = [
    ("Site-Info", "site_info", "imweb_site_info", "사이트 정보"),
    ("Member-Info", "member_info", "imweb_member_info", "회원 정보"),
    ("Community", "community", "imweb_community", "커뮤니티 (폼/Q&A/구매평)"),
    ("Promotion", "promotion", "imweb_promotion", "프로모션 (적립금/쿠폰)"),
    ("Product", "product", "imweb_product", "상품"),
    ("Order", "order", "imweb_order", "주문"),
    ("Script", "script", "imweb_script", "스크립트"),
    ("Payment", "payment", "imweb_payment", "결제"),
]
methods = ("get", "post", "patch", "put", "delete")


def load_spec():
    return json.loads(SPEC_FILE.read_text("utf-8"))


def split_ctrl(op_id: str) -> str:
    m = re.match(r"^[A-Za-z0-9]+Controller_(.+)$", op_id)
    return m.group(1) if m else op_id


def camel_to_snake(s: str) -> str:
    s = re.sub(r"(?<!^)(?=[A-Z][a-z])", "_", s)
    s = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", s)
    return re.sub(r"_+", "_", s).lower().strip("_")


def ref_name(r):
    return r["$ref"].split("/")[-1] if isinstance(r, dict) and "$ref" in r else None


def resolve_schema(spec, name):
    return (spec.get("components", {}).get("schemas", {}) or {}).get(name)


def body_schema_doc(spec, op) -> list[str]:
    """Return docstring lines describing the request body schema, or []."""
    rb = op.get("requestBody")
    if not rb:
        return []
    content = rb.get("content", {})
    app = content.get("application/json") or content.get("multipart/form-data")
    if not app:
        return []
    s = app.get("schema", {}) or {}
    name = ref_name(s)
    sch = resolve_schema(spec, name) if name else s
    name = name or "inline"
    if not isinstance(sch, dict):
        return [f"body ({name}): (스키마 확인)"]
    props = sch.get("properties") or {}
    req = sch.get("required") or []
    if not props:
        return [f"body ({name})"]
    lines = [f"body ({name}):"]
    for pn, ps in list(props.items()):
        t = _type_str(ps)
        desc = (ps.get("description") or "").strip().replace("\n", " ")[:80]
        mark = " 필수" if pn in req else ""
        line = f"  - {pn} ({t}{mark})"
        if desc:
            line += f": {desc}"
        lines.append(line)
    return lines


def _type_str(s):
    if not s:
        return "str"
    if "$ref" in s:
        return "dict"
    t = s.get("type")
    if t in ("integer", "number"):
        return "int" if t == "integer" else "float"
    if t == "boolean":
        return "bool"
    if t == "array":
        return "list"
    if t == "object":
        return "dict"
    return "str"


def collect(spec):
    by_cat = defaultdict(list)
    for path, item in spec.get("paths", {}).items():
        if not isinstance(item, dict):
            continue
        for m in methods:
            if m in item:
                op = item[m]
                tag = (op.get("tags") or ["Untagged"])[0]
                if tag == "OAuth2.0":
                    continue  # authorize/token handled internally (env + auth.py)
                op_id = op.get("operationId") or f"{m}_{path}"
                action = camel_to_snake(split_ctrl(op_id))
                pparams = [p["name"] for p in op.get("parameters", []) if p.get("in") == "path"]
                qparams = [p["name"] for p in op.get("parameters", []) if p.get("in") == "query"]
                has_body = bool(op.get("requestBody"))
                summary = (op.get("summary") or "").strip() or f"{m.upper()} {path}"
                by_cat[tag].append({
                    "action": action,
                    "method": m.upper(),
                    "path": path,
                    "pparams": pparams,
                    "qparams": qparams,
                    "has_body": has_body,
                    "summary": summary,
                    "body_lines": body_schema_doc(spec, op),
                })
    return by_cat


def render_module(tag, slug, tool_name, label, ops):
    out = []
    out.append(f'"""Generated tools — {tag} ({label}). DO NOT EDIT; regenerate via tools/_generator.py."""')
    out.append("from __future__ import annotations")
    out.append("")
    out.append("from typing import Literal")
    out.append("")
    out.append("from .._app import mcp")
    out.append("from .._base import get_client")
    out.append("")
    # _OPS table — action -> (method, path, [path_params], [query_params], has_body)
    out.append("# action -> (method, path, path_params, query_params, has_body)")
    out.append("_OPS: dict[str, tuple] = {")
    for o in ops:
        out.append(
            f'    {o["action"]!r}: ({o["method"]!r}, {o["path"]!r}, {o["pparams"]!r}, {o["qparams"]!r}, {o["has_body"]!r}),'
        )
    out.append("}")
    out.append("")

    actions = [o["action"] for o in ops]
    literal = "Literal[" + ", ".join(f'"{a}"' for a in actions) + "]"

    # docstring
    doc = [f"{label} 도구 — {len(ops)}개 action 을 디스패치합니다.", ""]
    doc.append("Args:")
    doc.append(f"    action: 수행 작업 키 (아래 {len(ops)}개 중 하나).")
    doc.append("    params: path + query 파라미터 딕셔너리. 예: {\"orderNo\": \"ORD123\", \"page\": 1}")
    doc.append("    body: POST/PATCH/PUT 요청 본문 (dict). body 가 있는 action 은 아래 스키마 참고.")
    doc.append("    paginate: list 계열 GET 에서 전체 페이지를 자동 집계할지 (기본 False = 단일 페이지).")
    doc.append("")
    doc.append("Actions:")
    for o in ops:
        mark = "  [body]" if o["has_body"] else ""
        pp = f" path={o['pparams']}" if o["pparams"] else ""
        qp = f" query={o['qparams']}" if o["qparams"] else ""
        doc.append(f'    - {o["action"]}: {o["summary"]} [{o["method"]} {o["path"]}{pp}{qp}{mark}]')
    bodies = [o for o in ops if o["body_lines"]]
    if bodies:
        doc.append("")
        doc.append("Body schemas:")
        for o in bodies:
            doc.append(f"  [{o['action']}]")
            for ln in o["body_lines"]:
                doc.append(f"    {ln}")
    doc.append("")
    doc.append("Returns: API JSON.")
    docstring = "\n".join(doc)

    out.append("@mcp.tool()")
    out.append(f"def {tool_name}(action: {literal}, params: dict | None = None, body: dict | None = None, paginate: bool = False) -> dict:")
    out.append('    r"""' + docstring + '"""')
    out.append("    _method, _path, _pp, _qp, _has_body = _OPS[action]")
    out.append("    _params = params or {}")
    out.append("    _pp_val = {k: _params[k] for k in _pp if k in _params}")
    out.append("    _qp_val = {k: _params[k] for k in _qp if k in _params}")
    out.append("    _client = get_client()")
    out.append('    if paginate and _method == "GET":')
    out.append("        return _client.list_all_pages(_path, params=_qp_val or None)")
    out.append("    _kw = {}")
    out.append('    if _pp_val:\n        _kw["path_params"] = _pp_val')
    out.append('    if _qp_val:\n        _kw["params"] = _qp_val')
    out.append('    if _has_body:\n        _kw["json_body"] = body or {}')
    out.append("    return _client.request(_method, _path, **_kw)")
    out.append("")
    return "\n".join(out)


def main():
    spec = load_spec()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    by_cat = collect(spec)

    # action uniqueness within a tag
    collisions = []
    for tag, ops in by_cat.items():
        seen = set()
        for o in ops:
            if o["action"] in seen:
                collisions.append((tag, o["action"]))
            seen.add(o["action"])

    slugs = []
    total = 0
    for tag, slug, tool_name, label in CATS:
        ops = by_cat.get(tag, [])
        if not ops:
            continue
        slugs.append(slug)
        src = render_module(tag, slug, tool_name, label, ops)
        (OUT_DIR / f"{slug}.py").write_text(src + "\n", "utf-8")
        total += len(ops)

    # __init__.py imports every module so decorators register.
    init = ['"""Generated tools package — importing it registers all Imweb category tools."""']
    init.append("from __future__ import annotations")
    init.append("")
    for slug in slugs:
        init.append(f"from . import {slug}  # noqa: F401")
    init.append("")
    init.append("__all__ = [" + ", ".join(f'"{s}"' for s in slugs) + "]")
    (OUT_DIR / "__init__.py").write_text("\n".join(init) + "\n", "utf-8")

    # Per-category report
    print(f"generated {len(slugs)} category tools covering {total} actions")
    for tag, slug, _, label in CATS:
        n = len(by_cat.get(tag, []))
        if n:
            print(f"  {slug:12s} ({label}): imweb_{slug}({n} actions)")
    if collisions:
        print("ACTION COLLISIONS:", collisions)
    else:
        print("action keys unique per tag: OK")


if __name__ == "__main__":
    main()
