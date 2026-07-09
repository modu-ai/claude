"""Generated tools — Order (주문). DO NOT EDIT; regenerate via tools/_generator.py."""
from __future__ import annotations

from typing import Literal

from .._app import mcp
from .._base import get_client

# action -> (method, path, path_params, query_params, has_body)
_OPS: dict[str, tuple] = {
    'read_all_parcel_company_list': ('GET', '/orders/parcel-company-list', [], [], False),
    'read_all_shipping_place_list': ('GET', '/orders/shipping-places', [], ['unitCode', 'shippingPlaceCode', 'shippingPlaceName'], False),
    'read_all_order': ('GET', '/orders', [], ['isDeliveryHold', 'orderSectionStatus', 'deliveryType', 'deliveryPayType', 'startDeliverySendTime', 'endDeliverySendTime', 'startDeliveryCompleteTime', 'endDeliveryCompleteTime', 'startCancelRequestTime', 'endCancelRequestTime', 'page', 'limit', 'unitCode', 'saleChannel', 'isMember', 'memberUid', 'memberCode', 'orderType', 'ordererName', 'ordererCall', 'isFirst', 'isCancelReq', 'isRequestPayment', 'startWtime', 'endWtime', 'isGift', 'shippingPlaceCode', 'paymentMethod', 'paymentStatus', 'includeOrderPending'], False),
    'read_one_order_by_order_no': ('GET', '/orders/{orderNo}', ['orderNo'], [], False),
    'read_all_order_section': ('GET', '/orders/{orderNo}/order-sections', ['orderNo'], ['isDeliveryHold', 'orderSectionStatus', 'deliveryType', 'deliveryPayType', 'startDeliverySendTime', 'endDeliverySendTime', 'startDeliveryCompleteTime', 'endDeliveryCompleteTime', 'startCancelRequestTime', 'endCancelRequestTime'], False),
    'read_one_order_section': ('GET', '/orders/{orderNo}/order-section/{orderSectionCode}', ['orderNo', 'orderSectionCode'], [], False),
    'read_all_order_section_item': ('GET', '/orders/{orderNo}/order-section/{orderSectionCode}/order-section-items', ['orderNo', 'orderSectionCode'], [], False),
    'read_one_order_section_item': ('GET', '/orders/{orderNo}/order-section/{orderSectionCode}/order-section-item/{orderSectionItemNo}', ['orderNo', 'orderSectionCode', 'orderSectionItemNo'], [], False),
    'read_order_coupons': ('GET', '/orders/{orderNo}/coupons', ['orderNo'], [], False),
    'update_order_shipping_operation': ('PATCH', '/orders/{orderNo}/shipping-operation', ['orderNo'], [], True),
    'update_order_section_shipping_operation': ('PATCH', '/orders/{orderNo}/order-section/{orderSectionCode}/shipping-operation', ['orderNo', 'orderSectionCode'], [], True),
    'update_order_section_item_shipping_operation': ('PATCH', '/orders/{orderNo}/order-section-items/{orderSectionItemNo}/shipping-operation', ['orderNo', 'orderSectionItemNo'], [], True),
    'create_order_invoice': ('POST', '/orders/{orderNo}/invoice', ['orderNo'], [], True),
    'update_order_invoice': ('PATCH', '/orders/{orderNo}/invoice', ['orderNo'], [], True),
    'remove_order_invoice': ('DELETE', '/orders/{orderNo}/invoice', ['orderNo'], [], True),
    'create_order_section_invoice': ('POST', '/orders/{orderNo}/order-section/{orderSectionCode}/invoice', ['orderNo', 'orderSectionCode'], [], True),
    'update_order_section_invoice': ('PATCH', '/orders/{orderNo}/order-section/{orderSectionCode}/invoice', ['orderNo', 'orderSectionCode'], [], True),
    'remove_order_section_invoice': ('DELETE', '/orders/{orderNo}/order-section/{orderSectionCode}/invoice', ['orderNo', 'orderSectionCode'], [], False),
    'create_order_section_item_invoice': ('POST', '/orders/{orderNo}/order-section-items/{orderSectionItemNo}/invoice', ['orderNo', 'orderSectionItemNo'], [], True),
    'update_order_cancel_request': ('PATCH', '/orders/{orderNo}/cancel-request', ['orderNo'], [], True),
    'update_order_section_cancel_request': ('PATCH', '/orders/{orderNo}/order-section/{orderSectionCode}/cancel-request', ['orderNo', 'orderSectionCode'], [], True),
    'update_order_section_item_cancel_request': ('PATCH', '/orders/{orderNo}/order-section-items/{orderSectionItemNo}/cancel-request', ['orderNo', 'orderSectionItemNo'], [], True),
    'update_order_cancel_reject': ('PATCH', '/orders/{orderNo}/cancel-reject', ['orderNo'], [], True),
    'update_order_section_cancel_reject': ('PATCH', '/orders/{orderNo}/order-section/{orderSectionCode}/cancel-reject', ['orderNo', 'orderSectionCode'], [], True),
    'update_order_section_item_cancel_reject': ('PATCH', '/orders/{orderNo}/order-section-items/{orderSectionItemNo}/cancel-reject', ['orderNo', 'orderSectionItemNo'], [], True),
    'update_order_return_request': ('PATCH', '/orders/{orderNo}/return-request', ['orderNo'], [], True),
    'update_order_section_return_request': ('PATCH', '/orders/{orderNo}/order-section/{orderSectionCode}/return-request', ['orderNo', 'orderSectionCode'], [], True),
    'update_order_section_item_return_request': ('PATCH', '/orders/{orderNo}/order-section-items/{orderSectionItemNo}/return-request', ['orderNo', 'orderSectionItemNo'], [], True),
    'update_order_section_retrieve_complete': ('PATCH', '/orders/{orderNo}/order-section/{orderSectionCode}/retrieve-complete', ['orderNo', 'orderSectionCode'], [], False),
    'update_order_return_reject': ('PATCH', '/orders/{orderNo}/return-reject', ['orderNo'], [], True),
    'update_order_section_return_reject': ('PATCH', '/orders/{orderNo}/order-section/{orderSectionCode}/return-reject', ['orderNo', 'orderSectionCode'], [], True),
    'update_order_section_item_return_reject': ('PATCH', '/orders/{orderNo}/order-section-items/{orderSectionItemNo}/return-reject', ['orderNo', 'orderSectionItemNo'], [], True),
    'update_order_exchange_request': ('PATCH', '/orders/{orderNo}/exchange-request', ['orderNo'], [], True),
    'update_order_section_exchange_request': ('PATCH', '/orders/{orderNo}/order-section/{orderSectionCode}/exchange-request', ['orderNo', 'orderSectionCode'], [], True),
    'update_order_section_item_exchange_request': ('PATCH', '/orders/{orderNo}/order-section-items/{orderSectionItemNo}/exchange-request', ['orderNo', 'orderSectionItemNo'], [], True),
    'update_order_exchange_reject': ('PATCH', '/orders/{orderNo}/exchange-reject', ['orderNo'], [], True),
    'update_order_section_exchange_reject': ('PATCH', '/orders/{orderNo}/order-section/{orderSectionCode}/exchange-reject', ['orderNo', 'orderSectionCode'], [], True),
    'update_order_section_item_exchange_reject': ('PATCH', '/orders/{orderNo}/order-section-items/{orderSectionItemNo}/exchange-reject', ['orderNo', 'orderSectionItemNo'], [], False),
    'update_order_section_cancel_approve': ('PATCH', '/orders/{orderNo}/order-section/{orderSectionCode}/cancel-approve', ['orderNo', 'orderSectionCode'], [], True),
    'update_order_section_item_cancel_approve': ('PATCH', '/orders/{orderNo}/order-section-items/{orderSectionItemNo}/cancel-approve', ['orderNo', 'orderSectionItemNo'], [], True),
    'update_order_section_return_approve': ('PATCH', '/orders/{orderNo}/order-section/{orderSectionCode}/return-approve', ['orderNo', 'orderSectionCode'], [], True),
    'update_order_section_item_return_approve': ('PATCH', '/orders/{orderNo}/order-section-items/{orderSectionItemNo}/return-approve', ['orderNo', 'orderSectionItemNo'], [], True),
    'update_order_section_exchange_approve': ('PATCH', '/orders/{orderNo}/order-section/{orderSectionCode}/exchange-approve', ['orderNo', 'orderSectionCode'], [], True),
    'update_order_section_item_exchange_approve': ('PATCH', '/orders/{orderNo}/order-section-items/{orderSectionItemNo}/exchange-approve', ['orderNo', 'orderSectionItemNo'], [], True),
}

@mcp.tool()
def imweb_order(action: Literal["read_all_parcel_company_list", "read_all_shipping_place_list", "read_all_order", "read_one_order_by_order_no", "read_all_order_section", "read_one_order_section", "read_all_order_section_item", "read_one_order_section_item", "read_order_coupons", "update_order_shipping_operation", "update_order_section_shipping_operation", "update_order_section_item_shipping_operation", "create_order_invoice", "update_order_invoice", "remove_order_invoice", "create_order_section_invoice", "update_order_section_invoice", "remove_order_section_invoice", "create_order_section_item_invoice", "update_order_cancel_request", "update_order_section_cancel_request", "update_order_section_item_cancel_request", "update_order_cancel_reject", "update_order_section_cancel_reject", "update_order_section_item_cancel_reject", "update_order_return_request", "update_order_section_return_request", "update_order_section_item_return_request", "update_order_section_retrieve_complete", "update_order_return_reject", "update_order_section_return_reject", "update_order_section_item_return_reject", "update_order_exchange_request", "update_order_section_exchange_request", "update_order_section_item_exchange_request", "update_order_exchange_reject", "update_order_section_exchange_reject", "update_order_section_item_exchange_reject", "update_order_section_cancel_approve", "update_order_section_item_cancel_approve", "update_order_section_return_approve", "update_order_section_item_return_approve", "update_order_section_exchange_approve", "update_order_section_item_exchange_approve"], params: dict | None = None, body: dict | None = None, paginate: bool = False) -> dict:
    r"""주문 도구 — 44개 action 을 디스패치합니다.

Args:
    action: 수행 작업 키 (아래 44개 중 하나).
    params: path + query 파라미터 딕셔너리. 예: {"orderNo": "ORD123", "page": 1}
    body: POST/PATCH/PUT 요청 본문 (dict). body 가 있는 action 은 아래 스키마 참고.
    paginate: list 계열 GET 에서 전체 페이지를 자동 집계할지 (기본 False = 단일 페이지).

Actions:
    - read_all_parcel_company_list: 택배사 목록 조회 [GET /orders/parcel-company-list]
    - read_all_shipping_place_list: 출고/반품 교환지 목록 조회 [GET /orders/shipping-places query=['unitCode', 'shippingPlaceCode', 'shippingPlaceName']]
    - read_all_order: 주문 목록 조회 [GET /orders query=['isDeliveryHold', 'orderSectionStatus', 'deliveryType', 'deliveryPayType', 'startDeliverySendTime', 'endDeliverySendTime', 'startDeliveryCompleteTime', 'endDeliveryCompleteTime', 'startCancelRequestTime', 'endCancelRequestTime', 'page', 'limit', 'unitCode', 'saleChannel', 'isMember', 'memberUid', 'memberCode', 'orderType', 'ordererName', 'ordererCall', 'isFirst', 'isCancelReq', 'isRequestPayment', 'startWtime', 'endWtime', 'isGift', 'shippingPlaceCode', 'paymentMethod', 'paymentStatus', 'includeOrderPending']]
    - read_one_order_by_order_no: 주문 조회 [GET /orders/{orderNo} path=['orderNo']]
    - read_all_order_section: 주문 섹션 목록 조회 [GET /orders/{orderNo}/order-sections path=['orderNo'] query=['isDeliveryHold', 'orderSectionStatus', 'deliveryType', 'deliveryPayType', 'startDeliverySendTime', 'endDeliverySendTime', 'startDeliveryCompleteTime', 'endDeliveryCompleteTime', 'startCancelRequestTime', 'endCancelRequestTime']]
    - read_one_order_section: 주문 섹션 조회 [GET /orders/{orderNo}/order-section/{orderSectionCode} path=['orderNo', 'orderSectionCode']]
    - read_all_order_section_item: 주문 섹션아이템 목록 조회 [GET /orders/{orderNo}/order-section/{orderSectionCode}/order-section-items path=['orderNo', 'orderSectionCode']]
    - read_one_order_section_item: 주문 섹션아이템 조회 [GET /orders/{orderNo}/order-section/{orderSectionCode}/order-section-item/{orderSectionItemNo} path=['orderNo', 'orderSectionCode', 'orderSectionItemNo']]
    - read_order_coupons: 주문 쿠폰 목록 조회 [GET /orders/{orderNo}/coupons path=['orderNo']]
    - update_order_shipping_operation: 주문 배송 처리 [PATCH /orders/{orderNo}/shipping-operation path=['orderNo']  [body]]
    - update_order_section_shipping_operation: 주문 섹션 배송 처리 [PATCH /orders/{orderNo}/order-section/{orderSectionCode}/shipping-operation path=['orderNo', 'orderSectionCode']  [body]]
    - update_order_section_item_shipping_operation: 주문 섹션아이템 배송 처리 [PATCH /orders/{orderNo}/order-section-items/{orderSectionItemNo}/shipping-operation path=['orderNo', 'orderSectionItemNo']  [body]]
    - create_order_invoice: 주문 송장 등록 [POST /orders/{orderNo}/invoice path=['orderNo']  [body]]
    - update_order_invoice: 주문 송장 수정 [PATCH /orders/{orderNo}/invoice path=['orderNo']  [body]]
    - remove_order_invoice: 주문 송장 삭제 [DELETE /orders/{orderNo}/invoice path=['orderNo']  [body]]
    - create_order_section_invoice: 주문 섹션 송장 등록 [POST /orders/{orderNo}/order-section/{orderSectionCode}/invoice path=['orderNo', 'orderSectionCode']  [body]]
    - update_order_section_invoice: 주문 섹션 송장 수정 [PATCH /orders/{orderNo}/order-section/{orderSectionCode}/invoice path=['orderNo', 'orderSectionCode']  [body]]
    - remove_order_section_invoice: 주문 섹션 송장 삭제 [DELETE /orders/{orderNo}/order-section/{orderSectionCode}/invoice path=['orderNo', 'orderSectionCode']]
    - create_order_section_item_invoice: 주문 섹션아이템 송장 등록 [POST /orders/{orderNo}/order-section-items/{orderSectionItemNo}/invoice path=['orderNo', 'orderSectionItemNo']  [body]]
    - update_order_cancel_request: 주문 취소 접수 요청 [PATCH /orders/{orderNo}/cancel-request path=['orderNo']  [body]]
    - update_order_section_cancel_request: 주문 섹션 취소 접수 요청 [PATCH /orders/{orderNo}/order-section/{orderSectionCode}/cancel-request path=['orderNo', 'orderSectionCode']  [body]]
    - update_order_section_item_cancel_request: 주문 섹션아이템 취소 접수 요청 [PATCH /orders/{orderNo}/order-section-items/{orderSectionItemNo}/cancel-request path=['orderNo', 'orderSectionItemNo']  [body]]
    - update_order_cancel_reject: 주문 취소 거절 요청 [PATCH /orders/{orderNo}/cancel-reject path=['orderNo']  [body]]
    - update_order_section_cancel_reject: 주문 섹션 취소 거절 요청 [PATCH /orders/{orderNo}/order-section/{orderSectionCode}/cancel-reject path=['orderNo', 'orderSectionCode']  [body]]
    - update_order_section_item_cancel_reject: 주문 섹션아이템 취소 거절 요청 [PATCH /orders/{orderNo}/order-section-items/{orderSectionItemNo}/cancel-reject path=['orderNo', 'orderSectionItemNo']  [body]]
    - update_order_return_request: 주문 반품 접수 요청 [PATCH /orders/{orderNo}/return-request path=['orderNo']  [body]]
    - update_order_section_return_request: 주문 섹션 반품 접수 요청 [PATCH /orders/{orderNo}/order-section/{orderSectionCode}/return-request path=['orderNo', 'orderSectionCode']  [body]]
    - update_order_section_item_return_request: 주문 섹션아이템 반품 접수 요청 [PATCH /orders/{orderNo}/order-section-items/{orderSectionItemNo}/return-request path=['orderNo', 'orderSectionItemNo']  [body]]
    - update_order_section_retrieve_complete: 주문 반품/교환 접수 섹션 수거완료 처리 [PATCH /orders/{orderNo}/order-section/{orderSectionCode}/retrieve-complete path=['orderNo', 'orderSectionCode']]
    - update_order_return_reject: 주문 반품 거절 요청 [PATCH /orders/{orderNo}/return-reject path=['orderNo']  [body]]
    - update_order_section_return_reject: 주문 섹션 반품 거절 요청 [PATCH /orders/{orderNo}/order-section/{orderSectionCode}/return-reject path=['orderNo', 'orderSectionCode']  [body]]
    - update_order_section_item_return_reject: 주문 섹션아이템 반품 거절 요청 [PATCH /orders/{orderNo}/order-section-items/{orderSectionItemNo}/return-reject path=['orderNo', 'orderSectionItemNo']  [body]]
    - update_order_exchange_request: 주문 교환 접수 요청 [PATCH /orders/{orderNo}/exchange-request path=['orderNo']  [body]]
    - update_order_section_exchange_request: 주문 섹션 교환 접수 요청 [PATCH /orders/{orderNo}/order-section/{orderSectionCode}/exchange-request path=['orderNo', 'orderSectionCode']  [body]]
    - update_order_section_item_exchange_request: 주문 섹션아이템 교환 접수 요청 [PATCH /orders/{orderNo}/order-section-items/{orderSectionItemNo}/exchange-request path=['orderNo', 'orderSectionItemNo']  [body]]
    - update_order_exchange_reject: 주문 교환 거절 요청 [PATCH /orders/{orderNo}/exchange-reject path=['orderNo']  [body]]
    - update_order_section_exchange_reject: 주문 섹션 교환 거절 요청 [PATCH /orders/{orderNo}/order-section/{orderSectionCode}/exchange-reject path=['orderNo', 'orderSectionCode']  [body]]
    - update_order_section_item_exchange_reject: 주문 섹션아이템 교환 거절 요청 [PATCH /orders/{orderNo}/order-section-items/{orderSectionItemNo}/exchange-reject path=['orderNo', 'orderSectionItemNo']]
    - update_order_section_cancel_approve: 주문 섹션 취소 승인 요청 [PATCH /orders/{orderNo}/order-section/{orderSectionCode}/cancel-approve path=['orderNo', 'orderSectionCode']  [body]]
    - update_order_section_item_cancel_approve: 주문 섹션아이템 취소 승인 요청 [PATCH /orders/{orderNo}/order-section-items/{orderSectionItemNo}/cancel-approve path=['orderNo', 'orderSectionItemNo']  [body]]
    - update_order_section_return_approve: 주문 섹션 반품 승인 요청 [PATCH /orders/{orderNo}/order-section/{orderSectionCode}/return-approve path=['orderNo', 'orderSectionCode']  [body]]
    - update_order_section_item_return_approve: 주문 섹션아이템 반품 승인 요청 [PATCH /orders/{orderNo}/order-section-items/{orderSectionItemNo}/return-approve path=['orderNo', 'orderSectionItemNo']  [body]]
    - update_order_section_exchange_approve: 주문 섹션 교환 승인 요청 [PATCH /orders/{orderNo}/order-section/{orderSectionCode}/exchange-approve path=['orderNo', 'orderSectionCode']  [body]]
    - update_order_section_item_exchange_approve: 주문 섹션아이템 교환 승인 요청 [PATCH /orders/{orderNo}/order-section-items/{orderSectionItemNo}/exchange-approve path=['orderNo', 'orderSectionItemNo']  [body]]

Body schemas:
  [update_order_shipping_operation]
    body (UpdateOrderShippingOperationRequestDto):
      - orderSectionStatus (str 필수): 배송처리할 상태
      - orderSectionCodeList (list): 배송 처리할 주문 섹션 코드 리스트 (없다면 하위 섹션 모두 처리)
      - invoiceNo (str): 송장번호
      - parcelCompanyIdx (float): 택배사 고유 idx
  [update_order_section_shipping_operation]
    body (UpdateOrderSectionShippingOperationRequestDto):
      - orderSectionStatus (str 필수): 배송처리할 상태
      - orderSectionItemDataList (list): 배송 처리할 주문 섹션아이템 번호 및 수량
      - invoiceNo (str): 송장번호
      - parcelCompanyIdx (float): 택배사 고유 idx
  [update_order_section_item_shipping_operation]
    body (UpdateOrderSectionItemShippingOperationRequestDto):
      - orderSectionStatus (str 필수): 배송처리할 상태
      - qty (float): 변경하려는 수량 (배송대기 변경 요청일 경우에만 입력 가능)
      - invoiceNo (str): 송장번호
      - parcelCompanyIdx (float): 택배사 고유 idx
  [create_order_invoice]
    body (OrderInvoiceRequestDto):
      - allInvoiceNo (str): 하위 모든 섹션에 처리할 송장번호
      - allParcelCompanyIdx (float): 하위 모든 섹션에 처리할 택배사 고유 idx
      - orderSectionInvoiceDataList (list): 송장 처리할 섹션 정보 리스트 (없다면 하위 섹션 모두 allInvoiceNo, allParcelCompanyIdx 으로 처리)
  [update_order_invoice]
    body (OrderInvoiceRequestDto):
      - allInvoiceNo (str): 하위 모든 섹션에 처리할 송장번호
      - allParcelCompanyIdx (float): 하위 모든 섹션에 처리할 택배사 고유 idx
      - orderSectionInvoiceDataList (list): 송장 처리할 섹션 정보 리스트 (없다면 하위 섹션 모두 allInvoiceNo, allParcelCompanyIdx 으로 처리)
  [remove_order_invoice]
    body (RemoveOrderInvoiceRequestDto):
      - orderSectionCodeList (list): 송장 삭제할 섹션 코드 목록
  [create_order_section_invoice]
    body (OrderSectionInvoiceRequestDto):
      - allInvoiceNo (str): 하위 모든 섹션에 처리할 송장번호
      - allParcelCompanyIdx (float): 하위 모든 섹션에 처리할 택배사 고유 idx
      - orderSectionItemInvoiceDataList (list): 송장 처리할 섹션 아이템 정보 리스트 (없다면 allInvoiceNo, allParcelCompanyIdx 으로 처리)
  [update_order_section_invoice]
    body (UpdateOrderSectionInvoiceRequestDto):
      - invoiceNo (str 필수): 송장번호
      - parcelCompanyIdx (float 필수): 택배사 고유 idx
  [create_order_section_item_invoice]
    body (UpdateOrderSectionInvoiceRequestDto):
      - invoiceNo (str 필수): 송장번호
      - parcelCompanyIdx (float 필수): 택배사 고유 idx
  [update_order_cancel_request]
    body (UpdateOrderCancelRequestRequestDto):
      - cancelReason (str 필수): 취소 사유
      - cancelReasonDetail (str): 취소 사유 상세
      - orderSectionCodeList (list): 취소 처리할 주문 섹션 코드 리스트 (없다면 하위 섹션 모두 처리)
  [update_order_section_cancel_request]
    body (UpdateOrderSectionCancelRequestRequestDto):
      - cancelReason (str 필수): 취소 사유
      - cancelReasonDetail (str): 취소 사유 상세
      - orderSectionItemDataList (list): 섹션아이템 목록
  [update_order_section_item_cancel_request]
    body (UpdateOrderSectionItemCancelRequestRequestDto):
      - cancelReason (str 필수): 취소 사유
      - cancelReasonDetail (str): 취소 사유 상세
      - qty (float): 변경하려는 섹션아이템의 수량
  [update_order_cancel_reject]
    body (UpdateOrderCancelRequestRejectDto):
      - orderSectionCodeList (list): 취소 요청을 거절할 주문 섹션 코드 리스트 (없다면 하위 섹션 모두 처리)
      - invoiceNo (str): 외부채널 주문 시 필수 입력 - 송장번호
      - parcelCompanyIdx (float): 외부채널 주문 시 필수 입력 - 택배사 고유 idx
  [update_order_section_cancel_reject]
    body (UpdateOrderSectionCancelRejectRequestDto):
      - orderSectionItemDataList (list): 섹션아이템 목록
      - invoiceNo (str): 외부채널 주문 시 필수 입력 - 송장번호
      - parcelCompanyIdx (float): 외부채널 주문 시 필수 입력 - 택배사 고유 idx
  [update_order_section_item_cancel_reject]
    body (UpdateOrderSectionItemCancelRejectRequestDto):
      - invoiceNo (str): 외부채널 주문일 경우 취소 요청을 거절하며 배송을 동시에 진행해야 하는 정책에 따라,  해당 필드에 택배사를 함께 입력해야 합니다. 일반 주문의
      - parcelCompanyIdx (float): 외부채널 주문 시 필수 입력 - 택배사 고유 idx
  [update_order_return_request]
    body (UpdateOrderReturnRequestRequestDto):
      - retrieveType (str 필수): 수거타입
      - retrievePayType (str): 수거결제타입 (구매자 발송, 수동 수거신청일 경우 필수)
      - returnReason (str 필수): 반품 사유<br>        외부채널 주문일 경우 다음 사유들 중 하나를 입력해주세요     - PRODUCT_UNSATISFIED: 서비스 
      - returnReasonDetail (str): 반품 상세 사유
      - invoiceNo (str): 송장번호 (구매자 발송, 수동 수거신청일 경우 필수)
      - parcelCompanyIdx (float): 택배사 고유 idx (구매자 발송, 수동 수거신청일 경우 필수)
      - retrieveMemo (str): 수거 특이사항 메모 (수거 타입이 기타일 경우에만 입력 가능)
      - orderSectionCodeList (list): 반품접수 처리할 주문 섹션 코드 리스트 (없다면 하위 섹션 모두 처리)
  [update_order_section_return_request]
    body (UpdateOrderSectionReturnRequestRequestDto):
      - retrieveType (str 필수): 수거타입
      - retrievePayType (str): 수거결제타입 (구매자 발송, 수동 수거신청일 경우 필수)
      - returnReason (str 필수): 반품 사유<br>        외부채널 주문일 경우 다음 사유들 중 하나를 입력해주세요     - PRODUCT_UNSATISFIED: 서비스 
      - returnReasonDetail (str): 반품 상세 사유
      - invoiceNo (str): 송장번호 (구매자 발송, 수동 수거신청일 경우 필수)
      - parcelCompanyIdx (float): 택배사 고유 idx (구매자 발송, 수동 수거신청일 경우 필수)
      - retrieveMemo (str): 수거 특이사항 메모 (수거 타입이 기타일 경우에만 입력 가능)
      - orderSectionItemDataList (list): 섹션아이템 목록
  [update_order_section_item_return_request]
    body (UpdateOrderSectionItemReturnRequestRequestDto):
      - retrieveType (str 필수): 수거타입
      - retrievePayType (str): 수거결제타입 (구매자 발송, 수동 수거신청일 경우 필수)
      - returnReason (str 필수): 반품 사유<br>        외부채널 주문일 경우 다음 사유들 중 하나를 입력해주세요     - PRODUCT_UNSATISFIED: 서비스 
      - returnReasonDetail (str): 반품 상세 사유
      - invoiceNo (str): 송장번호 (구매자 발송, 수동 수거신청일 경우 필수)
      - parcelCompanyIdx (float): 택배사 고유 idx (구매자 발송, 수동 수거신청일 경우 필수)
      - retrieveMemo (str): 수거 특이사항 메모 (수거 타입이 기타일 경우에만 입력 가능)
      - qty (float): 변경하려는 섹션아이템의 수량
  [update_order_return_reject]
    body (UpdateOrderReturnRejectRequestDto):
      - orderSectionCodeList (list): 반품 요청을 거절할 주문 섹션 코드 리스트 (없다면 하위 섹션 모두 처리)
      - externalRejectReason (str): 외부 채널 주문 - 거절 사유 <br> 외부 채널 주문은 거절 사유를 입력해야 합니다.
  [update_order_section_return_reject]
    body (UpdateOrderSectionReturnRejectRequestDto):
      - orderSectionItemDataList (list): 섹션아이템 목록
      - externalRejectReason (str): 외부 채널 주문 - 거절 사유 <br> 외부 채널 주문은 거절 사유를 입력해야 합니다.
  [update_order_section_item_return_reject]
    body (UpdateOrderSectionItemReturnRejectRequestDto):
      - externalRejectReason (str): 외부 채널 주문 - 거절 사유 <br> 외부 채널 주문은 거절 사유를 입력해야 합니다.
  [update_order_exchange_request]
    body (UpdateOrderExchangeRequestRequestDto):
      - retrieveType (str 필수): 수거타입
      - retrievePayType (str): 수거결제타입 (구매자 발송, 수동 수거신청일 경우 필수)
      - invoiceNo (str): 송장번호 (구매자 발송, 수동 수거신청일 경우 필수)
      - parcelCompanyIdx (float): 택배사 고유 idx (구매자 발송, 수동 수거신청일 경우 필수)
      - retrieveMemo (str): 수거 특이사항 메모 (수거 타입이 기타일 경우에만 입력 가능)
      - exchangeReason (str 필수): 교환 사유
      - exchangeReasonDetail (str): 교환 상세 사유
      - orderSectionCodeList (list): 교환접수 처리할 주문 섹션 코드 리스트 (없다면 하위 섹션 모두 처리)
      - exchangeOptionData (list): 옵션 변경이 필요한 섹션/섹션아이템별 교환 옵션 정보 (없다면 현재 옵션으로 교환)
  [update_order_section_exchange_request]
    body (UpdateOrderSectionExchangeRequestRequestDto):
      - retrieveType (str 필수): 수거타입
      - retrievePayType (str): 수거결제타입 (구매자 발송, 수동 수거신청일 경우 필수)
      - invoiceNo (str): 송장번호 (구매자 발송, 수동 수거신청일 경우 필수)
      - parcelCompanyIdx (float): 택배사 고유 idx (구매자 발송, 수동 수거신청일 경우 필수)
      - retrieveMemo (str): 수거 특이사항 메모 (수거 타입이 기타일 경우에만 입력 가능)
      - exchangeReason (str 필수): 교환 사유
      - exchangeReasonDetail (str): 교환 상세 사유
      - orderSectionItemDataList (list): 섹션아이템 목록
  [update_order_section_item_exchange_request]
    body (UpdateOrderSectionItemExchangeRequestRequestDto):
      - retrieveType (str 필수): 수거타입
      - retrievePayType (str): 수거결제타입 (구매자 발송, 수동 수거신청일 경우 필수)
      - invoiceNo (str): 송장번호 (구매자 발송, 수동 수거신청일 경우 필수)
      - parcelCompanyIdx (float): 택배사 고유 idx (구매자 발송, 수동 수거신청일 경우 필수)
      - retrieveMemo (str): 수거 특이사항 메모 (수거 타입이 기타일 경우에만 입력 가능)
      - exchangeReason (str 필수): 교환 사유
      - exchangeReasonDetail (str): 교환 상세 사유
      - optionDetailCodes (list): 변경할 옵션 상세 코드 리스트
      - qty (float): 변경하려는 섹션아이템의 수량
  [update_order_exchange_reject]
    body (UpdateOrderExchangeRejectRequestDto):
      - orderSectionCodeList (list): 교환 요청을 거절할 주문 섹션 코드 리스트 (없다면 하위 섹션 모두 처리)
  [update_order_section_exchange_reject]
    body (UpdateOrderSectionExchangeRejectRequestDto):
      - orderSectionItemDataList (list): 섹션아이템 목록
  [update_order_section_cancel_approve]
    body (UpdateOrderSectionCancelApproveRequestDto):
      - returnedCoupons (list): 반환할 쿠폰 코드 목록
      - excludeRefundAmount (float): 환불에서 제외할 금액
      - excludeRefundPoint (float): 환불에서 제외할 적립금 금액 (requestedRefundAmount와 동시 입력 불가)
      - requestedRefundAmount (float): 환불할 금액 (excludeRefundAmount와 동시 입력 불가, 최소 환불 금액은 0원 초과)
      - externalCancelReason (str): 외부채널 주문 용 취소 사유
      - externalCancelReasonDetail (str): 외부채널 주문 전용 취소 사유 상세
  [update_order_section_item_cancel_approve]
    body (UpdateOrderSectionItemCancelApproveRequestDto):
      - returnedCoupons (list): 반환할 쿠폰 코드 목록
      - excludeRefundAmount (float): 환불에서 제외할 금액
      - excludeRefundPoint (float): 환불에서 제외할 적립금 금액 (requestedRefundAmount와 동시 입력 불가)
      - requestedRefundAmount (float): 환불할 금액 (excludeRefundAmount와 동시 입력 불가, 최소 환불 금액은 0원 초과)
      - externalCancelReason (str): 외부채널 주문 전용 취소 사유
      - externalCancelReasonDetail (str): 외부채널 주문 전용 취소 사유 상세
  [update_order_section_return_approve]
    body (UpdateOrderSectionReturnApproveRequestDto):
      - returnedCoupons (list): 반환할 쿠폰 코드 목록
      - excludeRefundAmount (float): 환불에서 제외할 적립금 금액 (requestedRefundAmount와 동시 입력 불가)
      - excludeRefundPoint (float): 환불에서 제외할 적립금 금액
      - requestedRefundAmount (float): 환불할 금액 (excludeRefundAmount와 동시 입력 불가, 최소 환불 금액은 0원 초과)
  [update_order_section_item_return_approve]
    body (UpdateOrderSectionItemReturnApproveRequestDto):
      - returnedCoupons (list): 반환할 쿠폰 코드 목록
      - excludeRefundAmount (float): 환불에서 제외할 적립금 금액 (requestedRefundAmount와 동시 입력 불가)
      - excludeRefundPoint (float): 환불에서 제외할 적립금 금액
      - requestedRefundAmount (float): 환불할 금액 (excludeRefundAmount와 동시 입력 불가, 최소 환불 금액은 0원 초과)
  [update_order_section_exchange_approve]
    body (UpdateOrderSectionExchangeApproveRequestDto):
      - requestedDeliveryAmount (float): 청구할 배송비 금액
      - excludeDeliveryAmount (float): 차감할 배송비 금액
  [update_order_section_item_exchange_approve]
    body (UpdateOrderSectionItemExchangeApproveRequestDto):
      - requestedDeliveryAmount (float): 청구할 배송비 금액
      - excludeDeliveryAmount (float): 차감할 배송비 금액

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

