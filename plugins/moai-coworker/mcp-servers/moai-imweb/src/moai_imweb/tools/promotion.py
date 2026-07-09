"""Generated tools — Promotion (프로모션 (적립금/쿠폰)). DO NOT EDIT; regenerate via tools/_generator.py."""
from __future__ import annotations

from typing import Literal

from .._app import mcp
from .._base import get_client

# action -> (method, path, path_params, query_params, has_body)
_OPS: dict[str, tuple] = {
    'read_member_shop_point_by_filter': ('GET', '/promotion/shop-point', [], ['page', 'limit', 'memberUid', 'pointType', 'pointValue', 'unitCode'], False),
    'read_member_shop_point_log': ('GET', '/promotion/shop-point-log', [], ['page', 'limit', 'type', 'memberUid', 'memberUids', 'adminUid', 'orderNo', 'timeType', 'timeValue', 'unitCode'], False),
    'change_shop_point_by_member': ('PUT', '/promotion/shop-point/change/member/{memberUid}', ['memberUid'], [], True),
    'change_shop_point_by_group_type': ('PUT', '/promotion/shop-point/change/type', [], [], True),
    'read_one_shop_coupon_by_coupon_code': ('GET', '/promotion/shop-coupon/{shopCouponCode}', ['shopCouponCode'], ['unitCode'], False),
    'read_shop_coupon_by_filter': ('GET', '/promotion/shop-coupon', [], ['page', 'limit', 'type', 'startDateType', 'startDateValue', 'endDateType', 'endDateValue', 'editDateType', 'editDateValue', 'isUnlimitedDate', 'unitCode'], False),
    'create_shop_coupon_definition': ('POST', '/promotion/shop-coupon', [], [], True),
    'create_shop_coupon': ('POST', '/promotion/shop-coupon/{couponCode}/issue', ['couponCode'], [], True),
    'create_shop_coupon_bulk': ('POST', '/promotion/shop-coupon/{couponCode}/issue/bulk', ['couponCode'], [], True),
    'create_shop_coupon_by_group_type': ('POST', '/promotion/shop-coupon/{couponCode}/issue/group', ['couponCode'], [], True),
    'read_coupon_issue_list': ('GET', '/promotion/shop-coupon/{shopCouponCode}/coupon-issue', ['shopCouponCode'], ['page', 'memberUid', 'startDateType', 'startDateValue', 'endDateType', 'endDateValue', 'isUse', 'unitCode', 'limit'], False),
    'read_shop_coupon_issue_target_list': ('GET', '/promotion/shop-coupon/{shopCouponCode}/coupon-issue-target', ['shopCouponCode'], ['page', 'limit', 'unitCode', 'memberUid'], False),
    'read_member_shop_coupon_issue_target_list': ('GET', '/promotion/shop-coupon/member/{memberUid}/coupon-issue-target', ['memberUid'], ['page', 'limit', 'unitCode'], False),
    'read_member_coupon_issue_list': ('GET', '/promotion/shop-coupon/member/{memberUid}/coupon-issue', ['memberUid'], ['page', 'limit', 'unitCode', 'isUse'], False),
}

@mcp.tool()
def imweb_promotion(action: Literal["read_member_shop_point_by_filter", "read_member_shop_point_log", "change_shop_point_by_member", "change_shop_point_by_group_type", "read_one_shop_coupon_by_coupon_code", "read_shop_coupon_by_filter", "create_shop_coupon_definition", "create_shop_coupon", "create_shop_coupon_bulk", "create_shop_coupon_by_group_type", "read_coupon_issue_list", "read_shop_coupon_issue_target_list", "read_member_shop_coupon_issue_target_list", "read_member_coupon_issue_list"], params: dict | None = None, body: dict | None = None, paginate: bool = False) -> dict:
    r"""프로모션 (적립금/쿠폰) 도구 — 14개 action 을 디스패치합니다.

Args:
    action: 수행 작업 키 (아래 14개 중 하나).
    params: path + query 파라미터 딕셔너리. 예: {"orderNo": "ORD123", "page": 1}
    body: POST/PATCH/PUT 요청 본문 (dict). body 가 있는 action 은 아래 스키마 참고.
    paginate: list 계열 GET 에서 전체 페이지를 자동 집계할지 (기본 False = 단일 페이지).

Actions:
    - read_member_shop_point_by_filter: 적립금 정보 조회 [GET /promotion/shop-point query=['page', 'limit', 'memberUid', 'pointType', 'pointValue', 'unitCode']]
    - read_member_shop_point_log: 적립금 이력 조회 [GET /promotion/shop-point-log query=['page', 'limit', 'type', 'memberUid', 'memberUids', 'adminUid', 'orderNo', 'timeType', 'timeValue', 'unitCode']]
    - change_shop_point_by_member: 회원별 적립금 지급/차감 처리 [PUT /promotion/shop-point/change/member/{memberUid} path=['memberUid']  [body]]
    - change_shop_point_by_group_type: 회원등급/쇼핑그룹별 적립금 지금/차감 처리 [PUT /promotion/shop-point/change/type  [body]]
    - read_one_shop_coupon_by_coupon_code: 쿠폰 조회 [GET /promotion/shop-coupon/{shopCouponCode} path=['shopCouponCode'] query=['unitCode']]
    - read_shop_coupon_by_filter: 쿠폰 목록 조회 [GET /promotion/shop-coupon query=['page', 'limit', 'type', 'startDateType', 'startDateValue', 'endDateType', 'endDateValue', 'editDateType', 'editDateValue', 'isUnlimitedDate', 'unitCode']]
    - create_shop_coupon_definition: 쿠폰 생성 [POST /promotion/shop-coupon  [body]]
    - create_shop_coupon: 쿠폰 발급 [POST /promotion/shop-coupon/{couponCode}/issue path=['couponCode']  [body]]
    - create_shop_coupon_bulk: 쿠폰 일괄 발급 [POST /promotion/shop-coupon/{couponCode}/issue/bulk path=['couponCode']  [body]]
    - create_shop_coupon_by_group_type: 회원등급/그룹별 쿠폰 발급 [POST /promotion/shop-coupon/{couponCode}/issue/group path=['couponCode']  [body]]
    - read_coupon_issue_list: 쿠폰별 발급 목록 조회 [GET /promotion/shop-coupon/{shopCouponCode}/coupon-issue path=['shopCouponCode'] query=['page', 'memberUid', 'startDateType', 'startDateValue', 'endDateType', 'endDateValue', 'isUse', 'unitCode', 'limit']]
    - read_shop_coupon_issue_target_list: 지정 발행 쿠폰 발행 대상 조회 [GET /promotion/shop-coupon/{shopCouponCode}/coupon-issue-target path=['shopCouponCode'] query=['page', 'limit', 'unitCode', 'memberUid']]
    - read_member_shop_coupon_issue_target_list: 회원별 지정 발행 쿠폰 목록 조회 [GET /promotion/shop-coupon/member/{memberUid}/coupon-issue-target path=['memberUid'] query=['page', 'limit', 'unitCode']]
    - read_member_coupon_issue_list: 회원별 쿠폰 발급 목록 조회 [GET /promotion/shop-coupon/member/{memberUid}/coupon-issue path=['memberUid'] query=['page', 'limit', 'unitCode', 'isUse']]

Body schemas:
  [change_shop_point_by_member]
    body (ChangeShopPointByMemberRequestDto):
      - unitCode (str 필수): 유닛 코드
      - changeType (str 필수): 변경 타입(지급/차감)
      - point (float 필수): 적립금
      - reason (str 필수): 사유
  [change_shop_point_by_group_type]
    body (ChangeShopPointByGroupRequestDto):
      - unitCode (str 필수): 유닛 코드
      - division (str 필수): 그룹 구분 타입
      - groupCode (str 필수): 그룹 코드
      - changeType (str 필수): 변경 타입(지급/차감)
      - point (float 필수): 적립금
      - reason (str 필수): 사유
  [create_shop_coupon_definition]
    body (inline)
  [create_shop_coupon]
    body (IssueShopCouponRequestDto):
      - unitCode (str 필수): 유닛 코드
      - memberUid (str 필수): 아임웹 회원 아이디
  [create_shop_coupon_bulk]
    body (IssueShopCouponBulkRequestDto):
      - unitCode (str 필수): 유닛 코드
      - memberUids (list 필수): 회원 아이디 목록. 최대 50명
  [create_shop_coupon_by_group_type]
    body (IssueShopCouponByGroupRequestDto):
      - unitCode (str 필수): 유닛 코드
      - division (str 필수): 그룹 구분 타입
      - groupCode (str 필수): 그룹 코드

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

