# moai-smartstore-mcp

네이버 커머스(스마트스토어) 전 도메인 운영/관리 MCP 서버 — 네이버 커머스 API 센터의 공식 API 를 MCP(Model Context Protocol) 도구로 노출하여, Cowork/Claude Code 환경에서 상품·주문·정산·문의·물류·판매자정보·커머스솔루션·통계 운영을 자연어로 수행.

> **공식 문서**: https://apicenter.commerce.naver.com — 인증·전자서명 규격은 공식 인증 문서(https://apicenter.commerce.naver.com/docs/auth)를 따른다.

## 개요

9개 도메인(~140 엔드포인트)을 MCP 도구로 래핑:

| 도메인 | 도구 예시 |
|-------|----------|
| 인증 | `smartstore_test_connection` |
| 상품 | `product_search`, `product_create`, `product_update_stock`, `product_change_status`, `category_list` … |
| 주문 | `order_list_product_orders`, `order_dispatch`, `order_return_approve`, `order_exchange_dispatch` … |
| 정산 | `settlement_daily`, `settlement_case`, `vat_daily` … |
| 문의 | `qna_list`, `qna_answer`, `customer_inquiry_answer` … |
| 물류/N배송 | `logistics_companies`, `sku_list`, `sku_get` … |
| 판매자정보 | `seller_account`, `seller_channels`, `addressbook_list` … |
| 커머스솔루션 | `solution_subscription_get`, `solution_approve` … |
| 통계 | `stats_marketing`, `stats_sales`, `stats_shopping`, `stats_customer_status` … |

전체 도구 목록은 `manifest.json` 참고.

## 설치 및 실행

```bash
# uvx로 직접 실행
uvx moai-smartstore-mcp

# 버전 확인
uvx moai-smartstore-mcp --version

# 개발 환경
pip install -e ".[dev]"
pytest tests/
```

## 환경변수

자격증명은 반드시 환경변수로 주입. 코드·manifest·로그에 하드코딩 절대 금지.

```bash
export NAVER_COMMERCE_CLIENT_ID="<애플리케이션 ID>"
export NAVER_COMMERCE_CLIENT_SECRET="<애플리케이션 시크릿(bcrypt salt)>"
export NAVER_COMMERCE_ACCOUNT_ID="<판매자 계정 ID>"   # type=SELLER 시 필수
export NAVER_COMMERCE_TYPE="SELF"                       # SELF(기본) | SELLER
```

발급 절차는 `CONNECTORS.md` 참고.

## 인증

OAuth2 Client Credentials Grant + bcrypt 전자서명.

- 전자서명 = `base64(bcrypt(client_id + "_" + timestamp, client_secret))`
- timestamp 는 밀리초 단위, 5분 유효.
- 401 + `GW.AUTHN` 응답 시 토큰 만료로 간주해 자동 재발급 후 1회 재시도.

## 라이선스

LicenseRef-MoAI-NC-ND-1.0 (cowork-plugins 정책 준용).
