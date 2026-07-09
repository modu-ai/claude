"""Generated tools — Script (스크립트). DO NOT EDIT; regenerate via tools/_generator.py."""
from __future__ import annotations

from typing import Literal

from .._app import mcp
from .._base import get_client

# action -> (method, path, path_params, query_params, has_body)
_OPS: dict[str, tuple] = {
    'read_script_by_unit_code': ('GET', '/script', [], ['unitCode', 'position'], False),
    'create_script': ('POST', '/script', [], [], True),
    'update_script': ('PUT', '/script', [], [], True),
    'delete_script': ('DELETE', '/script', [], ['unitCode', 'position'], False),
}

@mcp.tool()
def imweb_script(action: Literal["read_script_by_unit_code", "create_script", "update_script", "delete_script"], params: dict | None = None, body: dict | None = None, paginate: bool = False) -> dict:
    r"""스크립트 도구 — 4개 action 을 디스패치합니다.

Args:
    action: 수행 작업 키 (아래 4개 중 하나).
    params: path + query 파라미터 딕셔너리. 예: {"orderNo": "ORD123", "page": 1}
    body: POST/PATCH/PUT 요청 본문 (dict). body 가 있는 action 은 아래 스키마 참고.
    paginate: list 계열 GET 에서 전체 페이지를 자동 집계할지 (기본 False = 단일 페이지).

Actions:
    - read_script_by_unit_code: 스크립트 조회 [GET /script query=['unitCode', 'position']]
    - create_script: 스크립트 등록 [POST /script  [body]]
    - update_script: 스크립트 수정 [PUT /script  [body]]
    - delete_script: 스크립트 삭제 [DELETE /script query=['unitCode', 'position']]

Body schemas:
  [create_script]
    body (CreateScriptRequestDto):
      - unitCode (str 필수): 유닛 코드
      - position (str 필수): 스크립트 삽입 위치입니다. - header: 헤더 영역 - body: 바디 영역 - footer: 푸터 영역 - product_detail: 상
      - scriptContent (str 필수): 스크립트 내용
  [update_script]
    body (UpdateScriptRequestDto):
      - unitCode (str 필수): 유닛 코드
      - position (str 필수): 스크립트 삽입 위치입니다. - header: 헤더 영역 - body: 바디 영역 - footer: 푸터 영역 - product_detail: 상
      - scriptContent (str 필수): 스크립트 내용

Returns: API JSON."""
    _method, _path, _pp, _qp, _has_body = _OPS[action]
    _params = params or {}
    _pp_val = {k: _params[k] for k in _pp if k in _params}
    _qp_val = {k: _params[k] for k in _qp if k in _params}
    _client = get_client()
    if paginate and _method == "GET":
        return _client.list_all_pages(_path, params=_qp_val or None)
    _kw = {}
    if _pp_val:
        _kw["path_params"] = _pp_val
    if _qp_val:
        _kw["params"] = _qp_val
    if _has_body:
        _kw["json_body"] = body or {}
    return _client.request(_method, _path, **_kw)

