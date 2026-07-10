---
title: "「사무관」 — 문서·데이터 담당"
weight: 6
description: "HWPX·DOCX·XLSX·PPTX 등 한국형 오피스 문서와 공공데이터 조회를 담당하는 사무·데이터 AI 직원."
---

사무실의 하루 절반은 문서와 씨름하는 시간입니다. 한글(HWPX) 공문, 엑셀 정리, 파워포인트 보고, 그리고 "이 통계 어디서 찾지?"라는 검색까지. 사무관은 이 모든 서류 업무를 받아 주는 직원입니다. 관공서 민원실의 베테랑 주무관처럼, 어떤 서식이 와도 당황하지 않고 형식에 맞춰 처리해 주는 것이 강점입니다.

스킬은 31종으로 15명 중 가장 많습니다. 문서 계열은 HWPX(한글 문서)·DOCX·XLSX·PPTX·PDF 생성과 문서 읽기·양식 채우기를, 데이터 계열은 부동산·법원 경매·한국 주식·KOSIS 국가통계·건축물대장 같은 공공데이터 조회와 시각화를, 생산성 계열은 목표 관리·습관 루틴·데일리 브리핑을 다룹니다. kordoc(한국 문서 처리)·korean-stats(KOSIS 통계)·archhub(건축물대장)·DART(전자공시) 네 개의 MCP(클로드가 외부 서비스와 연결되는 표준 통로)가 연동됩니다.

숫자와 인용이 들어가는 문서가 많은 만큼, 데이터 출처를 따로 검증하는 검수 직원이 붙어 있습니다.

```mermaid
flowchart LR
    A["요청<br/>(보고서 한글파일로)"] --> B["스킬 매칭"]
    B --> C["doc-producer<br/>문서·데이터 작업"]
    C --> D["data-auditor<br/>인용·수치 검증"]
    D --> E["산출물<br/>(HWPX·XLSX·리포트)"]
```

## 스킬 카탈로그

office-\* 문서/데이터 스킬과 general-\* 생산성 스킬의 전체 목록입니다.

{{< employee-skills "moai-officer" >}}

## 에이전트

**doc-producer**(실행 직원)가 보고서·슬라이드·양식 문서를 생산하고, **data-auditor**(검수 직원)가 읽기 전용으로 공공데이터 인용과 계산을 독립 검증합니다. 통계 수치가 들어간 보고서일수록 이 이중 확인이 빛을 발합니다.

{{< employee-agents "moai-officer" >}}

## 대표 시나리오 3선

**1. 통계 기반 보고서.** "우리 구 인구 추이를 KOSIS에서 찾아서 한글 보고서로 만들어줘"라고 하면 korean-stats MCP가 통계를 조회하고, `office-data-visualizer`가 차트를, `office-hwpx-writer`가 HWPX 문서를 만들어 줍니다.

**2. 부동산·경매 조사.** "이 주소 건축물대장이랑 최근 경매 이력 확인해줘"라고 요청하면 `office-building-ledger-search`와 `office-finance-court-auction-search`가 공공데이터를 조회해 조사 노트로 정리합니다.

**3. 발표 자료 변환.** "이 엑셀 데이터로 월간 실적 슬라이드 만들어줘"라고 하면 `office-data-explorer`가 데이터를 요약하고 `office-pptx-designer` 또는 `office-html-slide`가 발표 자료로 변환합니다.

**잘 안 될 때** — 공공데이터 조회가 실패하면 해당 API 키(공공데이터포털·KOSIS 등) 등록 여부를 먼저 확인하세요. `office-mcp-connector-setup` 스킬이 연동 설정 자체를 안내해 줍니다.

## MCP 연동

- **kordoc** — HWPX 등 한국형 문서의 생성·파싱·양식 채우기·직인 배치. 로컬 처리 중심이라 별도 자격증명이 없습니다.
- **korean-stats** — KOSIS 국가통계 검색·조회·시계열 분석. KOSIS API 키가 필요할 수 있습니다.
- **archhub** — 건축물대장 조회. 공공데이터포털 API 키가 필요합니다.
- **dart** — 전자공시(DART) 기업 공시 조회. OpenDART API 키가 필요합니다.
