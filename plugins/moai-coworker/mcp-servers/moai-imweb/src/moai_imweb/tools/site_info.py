"""Generated tools — Site-Info (사이트 정보). DO NOT EDIT; regenerate via tools/_generator.py."""
from __future__ import annotations

from typing import Literal

from .._app import mcp
from .._base import get_client

# action -> (method, path, path_params, query_params, has_body)
_OPS: dict[str, tuple] = {
    'read_one_site_info_by_site_code': ('GET', '/site-info', [], [], False),
    'read_site_menu_list': ('GET', '/site-info/menu', [], ['unitCode'], False),
    'read_one_unit_info_by_unit_code': ('GET', '/site-info/unit/{unitCode}', ['unitCode'], [], False),
    'update_ground_app_integration_complete': ('PATCH', '/site-info/integration-complete', [], [], True),
    'update_ground_app_integration_cancellation': ('PATCH', '/site-info/integration-cancellation', [], [], False),
    'update_ground_app_integration_info': ('PATCH', '/site-info/integration-info', [], [], True),
}

@mcp.tool()
def imweb_site_info(action: Literal["read_one_site_info_by_site_code", "read_site_menu_list", "read_one_unit_info_by_unit_code", "update_ground_app_integration_complete", "update_ground_app_integration_cancellation", "update_ground_app_integration_info"], params: dict | None = None, body: dict | None = None, paginate: bool = False) -> dict:
    r"""사이트 정보 도구 — 6개 action 을 디스패치합니다.

Args:
    action: 수행 작업 키 (아래 6개 중 하나).
    params: path + query 파라미터 딕셔너리. 예: {"orderNo": "ORD123", "page": 1}
    body: POST/PATCH/PUT 요청 본문 (dict). body 가 있는 action 은 아래 스키마 참고.
    paginate: list 계열 GET 에서 전체 페이지를 자동 집계할지 (기본 False = 단일 페이지).

Actions:
    - read_one_site_info_by_site_code: 사이트 정보 조회 [GET /site-info]
    - read_site_menu_list: 사이트 메뉴 목록 조회 [GET /site-info/menu query=['unitCode']]
    - read_one_unit_info_by_unit_code: 유닛 정보 조회 [GET /site-info/unit/{unitCode} path=['unitCode']]
    - update_ground_app_integration_complete: 연동완료 처리 [PATCH /site-info/integration-complete  [body]]
    - update_ground_app_integration_cancellation: 연동해제 처리 [PATCH /site-info/integration-cancellation]
    - update_ground_app_integration_info: 연동정보 수정 [PATCH /site-info/integration-info  [body]]

Body schemas:
  [update_ground_app_integration_complete]
    body (UpdateIntegrationCompleteRequestDto):
      - configData (dict): 연동에 필요한 데이터 아임웹과 협의된 앱만 전달해 주세요.
  [update_ground_app_integration_info]
    body (UpdateIntegrationInfoRequestDto):
      - configData (dict 필수): 연동에 필요한 데이터 아임웹과 협의된 앱만 전달해 주세요.

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

