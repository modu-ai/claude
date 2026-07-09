"""Generated tools — Product (상품). DO NOT EDIT; regenerate via tools/_generator.py."""
from __future__ import annotations

from typing import Literal

from .._app import mcp
from .._base import get_client

# action -> (method, path, path_params, query_params, has_body)
_OPS: dict[str, tuple] = {
    'read_all_shop_products_by_filter': ('GET', '/products', [], ['page', 'limit', 'categoryCode', 'prodName', 'prodStatus', 'prodType', 'usePreSale', 'productAddTimeType', 'productAddTime', 'productEditTimeType', 'productEditTime', 'unitCode'], False),
    'create_product': ('POST', '/products', [], [], True),
    'read_all_shop_categories_by_site_code_and_unit_code': ('GET', '/products/shop-categories', [], ['unitCode'], False),
    'read_all_shop_showcases_by_site_code': ('GET', '/products/shop-showcases', [], [], False),
    'read_all_shop_naver_categories': ('GET', '/products/shop-naver-categories', [], ['page', 'limit', 'naverCategoryName'], False),
    'update_multiple_product_status': ('PATCH', '/products/status', [], [], True),
    'read_all_shop_product_options_by_prod_no': ('GET', '/products/{prodNo}/options', ['prodNo'], ['page', 'limit', 'unitCode'], False),
    'read_shop_product_options_by_prod_no': ('GET', '/products/{prodNo}/options/{optionCode}', ['prodNo', 'optionCode'], ['unitCode'], False),
    'update_product_options': ('PATCH', '/products/{prodNo}/options/{optionCode}', ['prodNo', 'optionCode'], [], True),
    'read_shop_product_options_by_prod_nos': ('GET', '/products/options', [], ['unitCode', 'prodNos'], False),
    'read_one_shop_products_by_prod_no': ('GET', '/products/{prodNo}', ['prodNo'], ['unitCode'], False),
    'update_product_info_by_prod_no': ('PATCH', '/products/{prodNo}', ['prodNo'], [], True),
    'read_all_shop_product_option_details_by_prod_no': ('GET', '/products/{prodNo}/option-details', ['prodNo'], ['page', 'limit', 'unitCode'], False),
    'read_shop_product_option_details_by_prod_no': ('GET', '/products/{prodNo}/option-details/{optionDetailCode}', ['prodNo', 'optionDetailCode'], ['unitCode'], False),
    'update_product_option_details': ('PATCH', '/products/{prodNo}/option-details/{optionDetailCode}', ['prodNo', 'optionDetailCode'], [], True),
    'read_shipping_service_settings': ('GET', '/products/{prodNo}/shipping-service-settings', ['prodNo'], ['unitCode'], False),
    'update_product_relative_info': ('PATCH', '/products/{prodNo}/relative-info', ['prodNo'], [], True),
    'update_product_seo_info': ('PATCH', '/products/{prodNo}/seo', ['prodNo'], [], True),
    'read_all_shop_product_shipping_settings_by_prod_no': ('GET', '/products/{prodNo}/shipping-settings', ['prodNo'], ['unitCode'], False),
    'update_product_shipping_settings_by_prod_no': ('PATCH', '/products/{prodNo}/shipping-settings', ['prodNo'], [], True),
    'update_product_stock_info_by_prod_no': ('PATCH', '/products/{prodNo}/stock-info', ['prodNo'], [], True),
    'update_product_price_by_prod_no': ('PATCH', '/products/{prodNo}/price', ['prodNo'], [], True),
    'update_product_discount_info_by_prod_no': ('PATCH', '/products/{prodNo}/discount-info', ['prodNo'], [], True),
    'update_product_display_info_by_prod_no': ('PATCH', '/products/{prodNo}/display', ['prodNo'], [], True),
    'update_product_classification': ('PATCH', '/products/{prodNo}/classification', ['prodNo'], [], True),
    'update_product_status': ('PATCH', '/products/{prodNo}/status', ['prodNo'], [], True),
    'update_product_external_integration_info': ('PATCH', '/products/{prodNo}/external-integration-info', ['prodNo'], [], True),
    'update_product_additional_info': ('PATCH', '/products/{prodNo}/additional-info', ['prodNo'], [], True),
    'update_product_etc_info': ('PATCH', '/products/{prodNo}/etc-info', ['prodNo'], [], True),
    'update_product_exhibitions': ('PATCH', '/products/{prodNo}/exhibitions', ['prodNo'], [], True),
    'create_product_images': ('POST', '/products/{prodNo}/images', ['prodNo'], [], True),
}

@mcp.tool()
def imweb_product(action: Literal["read_all_shop_products_by_filter", "create_product", "read_all_shop_categories_by_site_code_and_unit_code", "read_all_shop_showcases_by_site_code", "read_all_shop_naver_categories", "update_multiple_product_status", "read_all_shop_product_options_by_prod_no", "read_shop_product_options_by_prod_no", "update_product_options", "read_shop_product_options_by_prod_nos", "read_one_shop_products_by_prod_no", "update_product_info_by_prod_no", "read_all_shop_product_option_details_by_prod_no", "read_shop_product_option_details_by_prod_no", "update_product_option_details", "read_shipping_service_settings", "update_product_relative_info", "update_product_seo_info", "read_all_shop_product_shipping_settings_by_prod_no", "update_product_shipping_settings_by_prod_no", "update_product_stock_info_by_prod_no", "update_product_price_by_prod_no", "update_product_discount_info_by_prod_no", "update_product_display_info_by_prod_no", "update_product_classification", "update_product_status", "update_product_external_integration_info", "update_product_additional_info", "update_product_etc_info", "update_product_exhibitions", "create_product_images"], params: dict | None = None, body: dict | None = None, paginate: bool = False) -> dict:
    r"""상품 도구 — 31개 action 을 디스패치합니다.

Args:
    action: 수행 작업 키 (아래 31개 중 하나).
    params: path + query 파라미터 딕셔너리. 예: {"orderNo": "ORD123", "page": 1}
    body: POST/PATCH/PUT 요청 본문 (dict). body 가 있는 action 은 아래 스키마 참고.
    paginate: list 계열 GET 에서 전체 페이지를 자동 집계할지 (기본 False = 단일 페이지).

Actions:
    - read_all_shop_products_by_filter: 상품 목록 조회 [GET /products query=['page', 'limit', 'categoryCode', 'prodName', 'prodStatus', 'prodType', 'usePreSale', 'productAddTimeType', 'productAddTime', 'productEditTimeType', 'productEditTime', 'unitCode']]
    - create_product: 상품 등록 [POST /products  [body]]
    - read_all_shop_categories_by_site_code_and_unit_code: 상품 카테고리 목록 조회 [GET /products/shop-categories query=['unitCode']]
    - read_all_shop_showcases_by_site_code: 상품 기획전 목록 조회 [GET /products/shop-showcases]
    - read_all_shop_naver_categories: 상품 네이버 카테고리 목록 조회 [GET /products/shop-naver-categories query=['page', 'limit', 'naverCategoryName']]
    - update_multiple_product_status: 상품 상태 일괄 수정 [PATCH /products/status  [body]]
    - read_all_shop_product_options_by_prod_no: 상품 옵션 목록 조회 [GET /products/{prodNo}/options path=['prodNo'] query=['page', 'limit', 'unitCode']]
    - read_shop_product_options_by_prod_no: 상품 옵션 조회 [GET /products/{prodNo}/options/{optionCode} path=['prodNo', 'optionCode'] query=['unitCode']]
    - update_product_options: 상품 옵션 수정 [PATCH /products/{prodNo}/options/{optionCode} path=['prodNo', 'optionCode']  [body]]
    - read_shop_product_options_by_prod_nos: 상품 옵션 일괄 조회 [GET /products/options query=['unitCode', 'prodNos']]
    - read_one_shop_products_by_prod_no: 상품 조회 [GET /products/{prodNo} path=['prodNo'] query=['unitCode']]
    - update_product_info_by_prod_no: 상품 상세 수정 [PATCH /products/{prodNo} path=['prodNo']  [body]]
    - read_all_shop_product_option_details_by_prod_no: 상품 옵션 상세 목록 조회 [GET /products/{prodNo}/option-details path=['prodNo'] query=['page', 'limit', 'unitCode']]
    - read_shop_product_option_details_by_prod_no: 상품 옵션 상세 조회 [GET /products/{prodNo}/option-details/{optionDetailCode} path=['prodNo', 'optionDetailCode'] query=['unitCode']]
    - update_product_option_details: 상품 옵션 상세 수정 [PATCH /products/{prodNo}/option-details/{optionDetailCode} path=['prodNo', 'optionDetailCode']  [body]]
    - read_shipping_service_settings: 상품 빠른 배송 설정 조회 [GET /products/{prodNo}/shipping-service-settings path=['prodNo'] query=['unitCode']]
    - update_product_relative_info: 상품 연관 상품 정보 수정 [PATCH /products/{prodNo}/relative-info path=['prodNo']  [body]]
    - update_product_seo_info: 상품 SEO 정보 수정 [PATCH /products/{prodNo}/seo path=['prodNo']  [body]]
    - read_all_shop_product_shipping_settings_by_prod_no: 상품 배송 설정 조회 [GET /products/{prodNo}/shipping-settings path=['prodNo'] query=['unitCode']]
    - update_product_shipping_settings_by_prod_no: 상품 배송 설정 수정 [PATCH /products/{prodNo}/shipping-settings path=['prodNo']  [body]]
    - update_product_stock_info_by_prod_no: 상품 재고 수정 [PATCH /products/{prodNo}/stock-info path=['prodNo']  [body]]
    - update_product_price_by_prod_no: 상품 가격 설정 수정 [PATCH /products/{prodNo}/price path=['prodNo']  [body]]
    - update_product_discount_info_by_prod_no: 상품 할인 설정 수정 [PATCH /products/{prodNo}/discount-info path=['prodNo']  [body]]
    - update_product_display_info_by_prod_no: 상품 외부 노출 설정 수정 [PATCH /products/{prodNo}/display path=['prodNo']  [body]]
    - update_product_classification: 상품 분류 정보 수정 [PATCH /products/{prodNo}/classification path=['prodNo']  [body]]
    - update_product_status: 상품 상태 수정 [PATCH /products/{prodNo}/status path=['prodNo']  [body]]
    - update_product_external_integration_info: 상품 외부 연동정보 수정 [PATCH /products/{prodNo}/external-integration-info path=['prodNo']  [body]]
    - update_product_additional_info: 상품 추가 상품 정보 수정 [PATCH /products/{prodNo}/additional-info path=['prodNo']  [body]]
    - update_product_etc_info: 상품 기타 설정 수정 [PATCH /products/{prodNo}/etc-info path=['prodNo']  [body]]
    - update_product_exhibitions: 상품 진열 설정 수정 [PATCH /products/{prodNo}/exhibitions path=['prodNo']  [body]]
    - create_product_images: 상품 이미지 업로드 [POST /products/{prodNo}/images path=['prodNo']  [body]]

Body schemas:
  [create_product]
    body (CreateShopProductRequestDto):
      - productImages (list 필수): 상품 이미지<br> 상품 등록 시 이미지는 최대 10개까지 등록할 수 있고, 더 추가하려면 상품 수정 API를 이용하시면 됩니다.
      - digitalImage (str): 디지털 상품 등록 시 업로드할 파일<br> 디지털 상품 파일은 최대 1개까지 업로드 할 수 있습니다.
      - externalIntegrationImage (str): 외부 연동 이미지<br> 외부 연동 이미지는 최대 1개까지 업로드 할 수 있습니다.
      - productBaseInfo (dict 필수): 상품 기본 정보 데이터
      - productClassificationInfo (dict 필수): 상품 분류 데이터
      - productPriceInfo (list 필수): 상품 가격 데이터
      - productDiscountInfo (list 필수): 상품 할인 설정 데이터
      - productShippingSettingInfo (list): 상품 배송 설정 데이터
      - productEtcInfo (dict): 상품 기타 정보 데이터
      - productExhibitionInfo (list): 상품 전시 설정 데이터
      - productSeoInfo (list): 상품 SEO 설정 데이터
      - productOptionInfo (dict): 상품 옵션 데이터
      - productExternalIntegrationInfo (dict): 상품 외부 연동 정보 데이터
  [update_multiple_product_status]
    body (UpdateMultipleShopProductStatusRequestDto):
      - status (str 필수): 상품 상태 코드
      - prodNos (list 필수): 수정할 상품 번호 리스트
  [update_product_options]
    body (UpdateShopProductOptionRequestDto):
      - unitCode (str 필수): 유닛코드
      - name (str): 옵션 명
      - optionValueList (list): 수정할 옵션 값 정보
  [update_product_info_by_prod_no]
    body (UpdateShopProductInfoRequestDto):
      - digitalProductFile (str): 디지털 상품 이미지
      - unitCode (str 필수): unitCode
      - productName (str): 상품명
      - summaryDescription (str): 상품 요약 설명
      - description (str): 상품 상세 설명
      - images (list): 상품 이미지 URL 목록
      - useMobileDescription (str): 모바일 상세 설명 사용 여부
      - mobileDescription (str): 모바일 상세 설명
      - commonHeaderSettingType (str): 상품 상세 상단 공통 설정 타입
      - commonHeaderCode (str): 상품 상세 상단 공통 설정 코드(상품 상세 상단 공통 설정 타입이 custom일 경우 필수)
      - commonFooterSettingType (str): 상품 상세 하단 공통 설정 타입
      - commonFooterCode (str): 상품 상세 하단 공통 설정 코드(상품 상세 하단 공통 설정 타입이 custom일 경우 필수)
      - customProductCode (str): 자체 상품 코드
      - productType (str): 판매 방식 설정
      - digitalData (dict): 디지털 상품 데이터
      - subscribeData (dict): 회원그룹 이용권 데이터
      - useSalesPeriod (str): 판매기간 사용 여부
      - salesStartDate (str): 판매 기간 시작일
      - salesEndDate (str): 판매 기간 종료일
      - productInfoNoticeType (str): 상품정보제공고시 타입
      - productInfoNotice (str): 상품정보제공고시
  [update_product_option_details]
    body (UpdateShopProductOptionDetailRequestDto):
      - unitCode (str 필수): 유닛코드
      - price (float): 옵션 가격
      - supplyPrice (float): 옵션 공급가 (원가)
      - stock (float): 변경할 재고 수량(+ or -)
      - stockSku (str): 재고관리 코드(SKU)
      - status (str): 옵션 상세 상태
  [update_product_relative_info]
    body (UpdateShopProductRelativeRequestDto):
      - relativeData (list 필수): 수정할 연관 상품 정보 리스트
  [update_product_seo_info]
    body (UpdateShopProductSeoInfoRequestDto):
      - unitCode (str 필수): 유닛코드
      - seoAccessBot (str): 상품 검색엔진 노출 여부
      - seoTitle (str): SEO(검색엔진 최적화) 제목
      - seoDescription (str): SEO(검색엔진 최적화) 설명
  [update_product_shipping_settings_by_prod_no]
    body (UpdateShopProductShippingSettingsRequestDto):
      - unitCode (str 필수): 유닛코드
      - weight (float): 상품 무게
      - useDefaultShippingTemplate (str): 기본 배송 템플릿 사용 여부
      - shippingTemplateCode (str): 선택할 배송 템플릿 코드
      - useShippingNoticeTemplate (str 필수): 배송 관련 안내 템플릿 사용 여부
      - notice (str): 배송 관련 안내
      - shippingSettingDataList (list): 국가별 상품 배송 설정
  [update_product_stock_info_by_prod_no]
    body (UpdateShopProductStockRequestDto):
      - stock (float): 변경할 재고 수량(+ or -)
      - customSkuCode (str): 판매자 임의설정 재고 관리 번호(코드)
      - isUseStock (str): 재고 관리 기능 사용 여부
      - isUnlimitedStock (str): 재고 소진 후에도 주문 가능 여부
  [update_product_price_by_prod_no]
    body (UpdateShopProductPriceRequestDto):
      - unitCode (str 필수): 유닛코드
      - supplyPrice (float): 상품 공급가 (원가)
      - isPriceTaxIncluded (str): 부가세 포함 여부
      - isPriceNone (str): 가격 없음 여부
      - price (float): 판매가
      - originalPrice (float): 정가
  [update_product_discount_info_by_prod_no]
    body (UpdateShopProductDiscountOptionRequestDto):
      - unitCode (str 필수): 유닛코드
      - coupon (str 필수): 쿠폰 할인 설정 여부
      - point (str 필수): 포인트 할인 설정 여부
      - shoppingGroup (str 필수): 쇼핑등급 할인 설정 여부
      - givePointType (str): 적립금 지급 기준 타입
      - pointCriteria (dict): 적립금 지급 기준 설정
      - period (str 필수): 즉시/기간 할인 설정 여부
      - periodData (dict): 기간 할인 설정 데이터
  [update_product_display_info_by_prod_no]
    body (UpdateShopProductDisplayRequestDto):
      - unitCode (str 필수): 유닛코드
      - display (list 필수): 노출 설정
  [update_product_classification]
    body (UpdateShopProductClassificationRequestDto):
      - badge (dict): 상품 뱃지 설정
      - categories (list): 상품 카테고리
      - showcases (list): 상품 기획전
      - origin (str): 원산지
      - maker (str): 제조사
      - brand (str): 브랜드
  [update_product_status]
    body (UpdateShopProductStatusRequestDto):
      - status (str 필수): 상품 상태 코드
  [update_product_external_integration_info]
    body (UpdateShopProductExternalIntegrationInfoRequestDto):
      - externalImage (str): 외부연동 이미지
      - productName (str): 외부 노출용 상품 명
      - eventDescription (str): 외부 노출용 이벤트 문구
      - naverCategoryCode (str): 네이버 연동 용 카테고리 코드
      - status (str): 외부 연동용 상품 상태
      - saleMethod (str): 외부 연동용 상품 판매 방식
      - parallelImport (str): 병행 수입 여부
      - orderMade (str): 주문제작 상품 여부
      - purchasingAgent (str): 구매 대행 여부
      - cultureBenefit (str): 도서공연비 소득공제 여부
  [update_product_additional_info]
    body (UpdateShopProductAdditionalRequestDto):
      - unitCode (str 필수): 유닛 코드
      - prodNos (list 필수): 수정할 추가 상품 번호 리스트
  [update_product_etc_info]
    body (UpdateShopProductEtcInfoRequestDto):
      - minimumPurchaseQuantity (float): 최소 구매수량
      - maximumPurchaseQuantity (float): 1회 구매 시 최대 수량
      - maximumPurchaseQuantityType (str): 1회 구매 수량 제한 타입 (주문 단위, 품목 단위)
      - memberMaximumPurchaseQuantity (float): 1인 구매 시 최대 수량
      - optionalLimitType (str): 0원 선택옵션 구매 시 최대 구매 제한 타입 (본 상품 구매 수량만큼 구매 가능, 최대 구매 수량 제한, 1개만 구매 가능)
      - optionalLimit (float): 0원 선택옵션 구매 시 최대 구매 수량 (optionalLimitType 이 limit인 경우에만 입력)
      - useUnipassNumber (str): 개인통관고유부호 설정 (기본 방법을 따름, 사용함, 사용 안함)
      - adultPurchase (str): 미성년자 구매 불가능 여부 (구매불가, 구매가능)
  [update_product_exhibitions]
    body (UpdateShopProductExhibitionsRequestDto):
      - unitCode (str 필수): 유닛코드
      - isDisplay (str 필수): 진열 여부
  [create_product_images]
    body (inline):
      - images (list): 업로드할 이미지 파일 목록

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

