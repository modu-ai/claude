# 사무관 (moai-officer)

사무·데이터 전담 AI 직원입니다. 한국형 오피스 문서(HWPX·DOCX·XLSX·PPTX·PDF)와 HTML 리포트/슬라이드 생성, 공공데이터 조회(부동산·경매·주식·KOSIS·건축물대장·전자공시), 데이터 탐색·시각화, 생산성 루틴까지 실무 스킬 31종을 하나의 플러그인으로 제공합니다. 슬래시 명령을 외울 필요 없이 자연어로 요청하면 매칭되는 스킬이 자동 호출됩니다.

**이런 분께 추천**: 사무직 · 기획자 · 자영업 운영자

## 설치

Claude Code에서 두 단계로 설치합니다:

```
claude plugin marketplace add modu-ai/claude
claude plugin install moai-officer@moai-claude
```

또는 Claude Code 세션 안에서:

```
/plugin marketplace add modu-ai/claude
/plugin install moai-officer
```

## 스킬 31종

호출 형식: `/moai-officer:office-<스킬명>` — 예: `/moai-officer:office-hwpx-writer`. 자연어 요청("주간 보고서 HWPX로 만들어줘")으로도 자동 매칭됩니다.

### 문서 생성 (8종)

| 스킬 | 역할 |
|------|------|
| `office-hwpx-writer` | 아래아한글(.hwpx) 공문서·기안서·품의서·보고서 작성, HWP→HWPX 변환 |
| `office-docx-generator` | 워드(.docx) 보고서·계약서·제안서·공문서 생성 |
| `office-xlsx-creator` | 엑셀(.xlsx) KPI 대시보드·매출 분석표·예산표·간트차트 생성 |
| `office-pptx-designer` | 파워포인트(.pptx) 발표 슬라이드 디자인 |
| `office-pdf-writer` | HTML/Markdown/JSON/텍스트 → PDF 변환 (디자인 보존) |
| `office-html-report` | 마크다운 보고서 → 단일 파일 HTML 리포트 |
| `office-html-slide` | 자체 완결형 단일 파일 HTML 슬라이드 덱 (인라인 SVG 인포그래픽) |
| `office-document-reader` | 한국 공문서(HWP·HWPX·PDF·XLSX·DOCX) 마크다운 파싱 — kordoc MCP |

### 공공데이터 조회 (6종)

| 스킬 | 역할 |
|------|------|
| `office-public-data-public-data` | 공공데이터포털(data.go.kr)·KOSIS 통계 정밀 조회·분석 — korean-stats MCP 우선 |
| `office-public-data-real-estate-search` | 국토교통부 실거래가·전월세 시세 조회 |
| `office-public-data-court-auction-search` | 대법원 법원경매 매각공고·사건번호 조회 |
| `office-public-data-korean-stock-search` | KRX 상장 종목 검색·기본정보·일별 시세 조회 |
| `office-building-ledger-search` | 건축물대장·건축인허가·공시가격·노후도 조회 — archhub MCP |
| `office-business-real-estate-search` | 상업업무용 부동산 실거래 조회 (→ real-estate-search 경유) |

### 데이터 분석·시각화 (3종)

| 스킬 | 역할 |
|------|------|
| `office-data-explorer` | CSV·Excel 데이터 프로파일링·품질 보고서 |
| `office-data-visualizer` | 인터랙티브 차트·대시보드(HTML) 생성 |
| `office-design-system-library` | 75개 브랜드 디자인 시스템 토큰을 HTML 산출물에 적용 |

### 생산성·업무 루틴 (10종)

| 스킬 | 역할 |
|------|------|
| `office-daily-briefing` | 업계 뉴스·시장 동향·오늘 할 일 아침 브리핑 |
| `office-goal-planner` | 목표 → 실천 계획 (12주 계획법·만다라트·개인 OKR) |
| `office-habit-routine` | 습관·루틴 설계, 습관 트래커 |
| `office-time-system` | 하루·주간 시간 설계 (블록식스·우선순위) |
| `office-retro-builder` | 주간·연말 회고 (KPT·한 줄 회고) |
| `office-notion-template-kit` | 노션 업무관리·목표·회고 템플릿 구조 설계 |
| `office-mcp-connector-setup` | Drive·Notion·Higgsfield 커넥터 인증·환경변수 가이드 |
| `office-data-public-data` | 공공데이터 조회 라우터 (→ public-data-public-data 경유) |
| `office-finance-court-auction-search` | 법원경매 조회 라우터 (→ public-data-court-auction-search 경유) |
| `office-finance-korean-stock-search` | 국내주식 조회 라우터 (→ public-data-korean-stock-search 경유) |

### 생활 지원 (4종)

| 스킬 | 역할 |
|------|------|
| `general-event-planner` | 행사·세미나·웨딩 기획, 예산·일정 관리 |
| `general-travel-planner` | 여행 일정·맛집·숙소·예산 설계 |
| `general-self-care` | 번아웃 점검·회복 자기돌봄 |
| `general-wellness-coach` | 운동·식단·육아·시니어 케어 코칭 |

> 이관 안내: `office-business-real-estate-search` · `office-data-public-data` · `office-finance-court-auction-search` · `office-finance-korean-stock-search` 4종은 구명칭 호환용 라우터로, 각각 위 표의 `office-public-data-*` 스킬로 연결됩니다.

## MCP 연동 4종

플러그인 루트 `.mcp.json`에 4개 MCP 서버가 선언되어 있습니다. 자격증명은 **환경변수로만** 설정하세요(파일에 키를 적지 않습니다).

| 서버 | 역할 | 키 발급 | 비고 |
|------|------|---------|------|
| `kordoc` | 한국 공문서 파서 — HWP·HWPX·PDF·XLSX·DOCX → Markdown, 표 재현·양식 채우기·OCR (8도구) | 불필요 | Node.js 18+ 필요, `npx -y kordoc mcp` 자동 실행 |
| `korean-stats` | KOSIS 국가통계 조회 — 92 키워드·시도/시군구 라우팅·출처(통계표 ID) 자동 인용 (14도구) | 불필요 (공용키 hosted) | remote 커넥터, URL 등록만으로 동작 |
| `archhub` | 국토교통부 건축HUB — 건축물대장·인허가·공시가격·노후도 (11도구) | 불필요 (공용키 hosted) | hosted 장애 시 로컬 대체: `uvx --from git+https://github.com/chrisryugj/archhub-mcp archhub-mcp` + `ARCHHUB_SERVICE_KEY`(data.go.kr 건축HUB 활용신청) |
| `dart` | OpenDART 전자공시 — 공시·재무·지분·XBRL·HWP/PDF 첨부 마크다운화 (15도구) | 필요: [opendart.fss.or.kr](https://opendart.fss.or.kr) 회원가입 → 인증키 신청(이메일 즉시, 일 20,000건 무료) → `DART_API_KEY` 환경변수 | Node.js 20.19+ 권장 |

## 에이전트 2종

| 에이전트 | 등급 | 역할 |
|----------|------|------|
| `doc-producer` | worker | 보고서·슬라이드·양식 문서·공공데이터 조사·시각화 산출물을 만드는 실무 에이전트. 목표 이해 → 계획 → office-*/general-* 스킬 선택 → 실행 → 검증의 에이전트 루프로 동작. 공공데이터 수치는 출처(통계표 ID·공시 번호) 인용 필수, 조회 실패 시 `[NOT_FOUND]` 명시 |
| `data-auditor` | read-only audit | 수치 출처·표/차트-원데이터 정합·공문서 규격·계산을 회의적으로 재검증하는 감사 에이전트. 증거 기반 PASS/FAIL 판정만 반환하며 파일을 수정하지 않음 |

## 라이선스

LicenseRef-MoAI-NC-ND-1.0 · © modu-ai (email@mo.ai.kr)
