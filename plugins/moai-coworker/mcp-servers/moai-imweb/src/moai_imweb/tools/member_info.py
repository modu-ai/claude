"""Generated tools — Member-Info (회원 정보). DO NOT EDIT; regenerate via tools/_generator.py."""
from __future__ import annotations

from typing import Literal

from .._app import mcp
from .._base import get_client

# action -> (method, path, path_params, query_params, has_body)
_OPS: dict[str, tuple] = {
    'read_member_info_list': ('GET', '/member-info/members', [], ['page', 'limit', 'joinTimeRangeType', 'joinTimeRangeValue', 'lastLoginTimeRangeType', 'lastLoginTimeRangeValue', 'unitCode', 'memberCode', 'memberUid', 'smsAgree', 'emailAgree', 'thirdPartyAgree', 'callnum'], False),
    'read_member_info_list_by_cursor': ('GET', '/member-info/members/cursor', [], ['joinTimeRangeType', 'joinTimeRangeValue', 'lastLoginTimeRangeType', 'lastLoginTimeRangeValue', 'cursor', 'direction', 'limit', 'unitCode', 'smsAgree', 'emailAgree', 'thirdPartyAgree', 'callnum', 'editTimeRangeType', 'editTimeRangeValue'], False),
    'read_all_shop_prod_wish_by_prod_no': ('GET', '/member-info/members/product/wish-list', [], ['page', 'limit', 'prodNo'], False),
    'read_all_shop_order_cart_by_prod_no': ('GET', '/member-info/members/product/carts', [], ['page', 'limit', 'prodNo', 'unitCode'], False),
    'read_one_member_info_by_unit_code_and_member_uid': ('GET', '/member-info/members/{memberUid}', ['memberUid'], ['unitCode'], False),
    'read_member_group_list_by_site_code': ('GET', '/member-info/groups', [], ['page', 'limit'], False),
    'read_member_group_member_list': ('GET', '/member-info/groups/{memberGroupCode}/members', ['memberGroupCode'], ['page', 'limit', 'unitCode'], False),
    'read_member_grade_list_by_site_code': ('GET', '/member-info/grades', [], ['page', 'limit'], False),
    'read_member_list_by_member_grade': ('GET', '/member-info/grades/members', [], ['page', 'limit', 'unitCode', 'isDefaultGrade', 'memberGradeCode'], False),
    'read_admin_group_list': ('GET', '/member-info/admin/groups', [], ['page', 'limit'], False),
    'read_admin_group_member_list': ('GET', '/member-info/admin/groups/{siteGroupCode}/members', ['siteGroupCode'], ['page', 'limit', 'unitCode'], False),
    'read_one_admin_info_by_admin_uid': ('GET', '/member-info/admin/{adminUid}', ['adminUid'], [], False),
    'update_member_agree_info': ('PATCH', '/member-info/members/{memberUid}/agree-info', ['memberUid'], [], True),
    'update_member_group': ('PUT', '/member-info/members/{memberUid}/groups', ['memberUid'], [], True),
    'bulk_update_member_group': ('PUT', '/member-info/members/groups/bulk', [], [], True),
    'update_member_grade_by_member_uid': ('PUT', '/member-info/members/{memberUid}/grade', ['memberUid'], [], True),
    'bulk_update_member_grade': ('PUT', '/member-info/members/grades/bulk', [], [], True),
    'read_all_shop_prod_wish_by_member_uid': ('GET', '/member-info/members/{memberUid}/wish-list', ['memberUid'], [], False),
    'read_member_cart_list_by_member_uid': ('GET', '/member-info/members/{memberUid}/carts', ['memberUid'], ['unitCode'], False),
}

@mcp.tool()
def imweb_member_info(action: Literal["read_member_info_list", "read_member_info_list_by_cursor", "read_all_shop_prod_wish_by_prod_no", "read_all_shop_order_cart_by_prod_no", "read_one_member_info_by_unit_code_and_member_uid", "read_member_group_list_by_site_code", "read_member_group_member_list", "read_member_grade_list_by_site_code", "read_member_list_by_member_grade", "read_admin_group_list", "read_admin_group_member_list", "read_one_admin_info_by_admin_uid", "update_member_agree_info", "update_member_group", "bulk_update_member_group", "update_member_grade_by_member_uid", "bulk_update_member_grade", "read_all_shop_prod_wish_by_member_uid", "read_member_cart_list_by_member_uid"], params: dict | None = None, body: dict | None = None, paginate: bool = False) -> dict:
    r"""회원 정보 도구 — 19개 action 을 디스패치합니다.

Args:
    action: 수행 작업 키 (아래 19개 중 하나).
    params: path + query 파라미터 딕셔너리. 예: {"orderNo": "ORD123", "page": 1}
    body: POST/PATCH/PUT 요청 본문 (dict). body 가 있는 action 은 아래 스키마 참고.
    paginate: list 계열 GET 에서 전체 페이지를 자동 집계할지 (기본 False = 단일 페이지).

Actions:
    - read_member_info_list: 회원 목록 조회 [GET /member-info/members query=['page', 'limit', 'joinTimeRangeType', 'joinTimeRangeValue', 'lastLoginTimeRangeType', 'lastLoginTimeRangeValue', 'unitCode', 'memberCode', 'memberUid', 'smsAgree', 'emailAgree', 'thirdPartyAgree', 'callnum']]
    - read_member_info_list_by_cursor: 회원 목록 조회 (Cursor 기반) [GET /member-info/members/cursor query=['joinTimeRangeType', 'joinTimeRangeValue', 'lastLoginTimeRangeType', 'lastLoginTimeRangeValue', 'cursor', 'direction', 'limit', 'unitCode', 'smsAgree', 'emailAgree', 'thirdPartyAgree', 'callnum', 'editTimeRangeType', 'editTimeRangeValue']]
    - read_all_shop_prod_wish_by_prod_no: 위시리스트 상품 별 회원 목록 조회 [GET /member-info/members/product/wish-list query=['page', 'limit', 'prodNo']]
    - read_all_shop_order_cart_by_prod_no: 장바구니 상품 별 회원 목록 조회 [GET /member-info/members/product/carts query=['page', 'limit', 'prodNo', 'unitCode']]
    - read_one_member_info_by_unit_code_and_member_uid: 회원 조회 [GET /member-info/members/{memberUid} path=['memberUid'] query=['unitCode']]
    - read_member_group_list_by_site_code: 회원 그룹 목록 조회 [GET /member-info/groups query=['page', 'limit']]
    - read_member_group_member_list: 회원 그룹별 회원 목록 조회 [GET /member-info/groups/{memberGroupCode}/members path=['memberGroupCode'] query=['page', 'limit', 'unitCode']]
    - read_member_grade_list_by_site_code: 회원 쇼핑 등급 목록 조회 [GET /member-info/grades query=['page', 'limit']]
    - read_member_list_by_member_grade: 회원 쇼핑 등급별 회원 목록 조회 [GET /member-info/grades/members query=['page', 'limit', 'unitCode', 'isDefaultGrade', 'memberGradeCode']]
    - read_admin_group_list: 운영진 그룹 목록 조회 [GET /member-info/admin/groups query=['page', 'limit']]
    - read_admin_group_member_list: 운영진 그룹별 회원 목록 조회 [GET /member-info/admin/groups/{siteGroupCode}/members path=['siteGroupCode'] query=['page', 'limit', 'unitCode']]
    - read_one_admin_info_by_admin_uid: 운영진 조회 [GET /member-info/admin/{adminUid} path=['adminUid']]
    - update_member_agree_info: 회원 동의 정보 수정 [PATCH /member-info/members/{memberUid}/agree-info path=['memberUid']  [body]]
    - update_member_group: 회원 그룹 변경 [PUT /member-info/members/{memberUid}/groups path=['memberUid']  [body]]
    - bulk_update_member_group: 회원 그룹 일괄 변경 [PUT /member-info/members/groups/bulk  [body]]
    - update_member_grade_by_member_uid: 회원 등급 변경 [PUT /member-info/members/{memberUid}/grade path=['memberUid']  [body]]
    - bulk_update_member_grade: 회원 등급 일괄 변경 [PUT /member-info/members/grades/bulk  [body]]
    - read_all_shop_prod_wish_by_member_uid: 회원 위시리스트 조회 [GET /member-info/members/{memberUid}/wish-list path=['memberUid']]
    - read_member_cart_list_by_member_uid: 회원 장바구니 목록 조회 [GET /member-info/members/{memberUid}/carts path=['memberUid'] query=['unitCode']]

Body schemas:
  [update_member_agree_info]
    body (UpdateMemberAgreeInfoRequest):
      - smsAgree (str): sms 수신 동의 여부
      - emailAgree (str): email 수신 동의 여부
      - thirdPartyAgree (str): 제 3자 정보제공 동의 여부
  [update_member_group]
    body (UpdateMemberGroupRequestDto):
      - unitCode (str 필수): 유닛 코드
      - groupCodes (list 필수): 변경할 회원 그룹 코드 리스트
  [bulk_update_member_group]
    body (BulkUpdateMemberGroupRequestDto):
      - unitCode (str 필수): 유닛 코드
      - memberUids (list 필수): 그룹을 변경할 회원 ID 목록 (최대 30건)
      - groupCodes (list 필수): 최종 적용할 회원 그룹 코드 리스트
  [update_member_grade_by_member_uid]
    body (UpdateMemberGradeRequestDto):
      - unitCode (str 필수): 유닛 코드
      - isDefaultGrade (str 필수): 기본 등급 여부
      - useAutoGrade (str): 자동 등급 사용 여부
      - memberGradeCode (str 필수): 변경할 회원 등급 코드
  [bulk_update_member_grade]
    body (BulkUpdateMemberGradeRequestDto):
      - unitCode (str 필수): 유닛 코드
      - memberUids (list 필수): 등급을 변경할 회원 ID 목록 (최대 30건)
      - isDefaultGrade (str 필수): 기본 등급 여부
      - useAutoGrade (str): 자동 등급 사용 여부
      - memberGradeCode (str): 변경할 회원 등급 코드

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

