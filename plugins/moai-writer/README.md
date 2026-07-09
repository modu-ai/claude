# 작가 (moai-writer)

작가/IP 창작 전담 AI 직원입니다. 출판 기획·집필(book-* 8종), 웹툰·웹소설·시나리오·콘티·표지·IP 사업화(story-* 13종), 한국어 인문화 윤문과 맞춤법 검수까지 창작 전 과정 스킬 23종을 하나의 플러그인으로 제공합니다. 슬래시 명령을 외울 필요 없이 자연어로 요청하면 매칭되는 스킬이 자동 호출됩니다. 이 스킬들은 moai-coworker에서 이관되었습니다.

**이런 분께 추천**: 작가 · 웹툰/웹소설 창작자 · 1인 출판인

## 설치

Claude Code에서 두 단계로 설치합니다:

```
claude plugin marketplace add modu-ai/claude
claude plugin install moai-writer@moai-claude
```

또는 Claude Code 세션 안에서:

```
/plugin marketplace add modu-ai/claude
/plugin install moai-writer
```

## 스킬 23종

호출 형식: `/moai-writer:<스킬명>` — 예: `/moai-writer:book-concept-planner`. 자연어 요청("책 컨셉서 만들어줘")으로도 자동 매칭됩니다.

### 출판 (book-* 8종)

| 스킬 | 역할 |
|------|------|
| `book-concept-planner` | 출판사 제출용 도서 컨셉서 작성 (한 줄·30자·300자 요약, USP 3축, 시장 포지셔닝) |
| `book-target-reader` | 타깃 독자 페르소나·JTBD·페인포인트 매트릭스 설계 |
| `book-outline-designer` | 부·장·꼭지 3레벨 목차 설계 + 분량 배분 + 챕터 시놉시스 |
| `book-chapter-writer` | 챕터 초고 집필 — 꼭지 단위 작성·매수 관리·4 장르 문체 분기 |
| `book-revision-coach` | 퇴고·교열 코치 — 어법·문체·논리·인용·분량 7단계 점검 |
| `book-author-bio` | 저자 약력·저자의 말 통합 작성 (50/200/500자 3길이) |
| `book-proposal-writer` | 출판사 투고용 제안서 — 기획서 + 샘플 챕터 + 마케팅 플랜 통합 |
| `book-publisher-matcher` | 한국 출판사 매칭 — 장르·규모·계약·인세 4차원 평가로 Top 5 추천 |

### 웹툰·웹소설·시나리오·IP (story-* 13종)

| 스킬 | 역할 |
|------|------|
| `story-project` | 작품 유형 분류 후 알맞은 story-* 파이프라인으로 라우팅하는 진입점 |
| `story-synopsis` | 시놉시스 — 로그라인·기획의도·인물 소개·회차/막 구성 |
| `story-screenplay` | 시나리오 — 씬 넘버·지문·대사를 한국 방송·영화 표준 포맷으로 작성 |
| `story-webtoon-planner` | 웹툰 기획 — 세계관·캐릭터·시즌/회차 구성·플랫폼 문법 설계 |
| `story-webtoon-episode` | 웹툰 회차 대본 — 컷 분할·대사·연출·말칸 배치 설계 |
| `story-webtoon-art` | 웹툰 패널 작화 — Higgsfield Soul ID로 캐릭터 일관성 유지 컷 생성 |
| `story-webnovel-writer` | 웹소설 연재 집필 — 문피아·카카오페이지 문법, 회차 절단 설계 |
| `story-character-sheet` | 캐릭터 시트 — 인물 설정 + Higgsfield Soul ID 비주얼 학습 |
| `story-conti` | 콘티·스토리보드 — 씬을 프레임 시퀀스로 분해해 이미지 생성 |
| `story-ad-conti` | 광고 콘티 — 제품·브랜드 스토리보드를 Higgsfield로 생성 |
| `story-previz` | 시네마틱 프리비즈 — 카메라·렌즈·조명 지정 숏 생성 |
| `story-cover-art` | 표지·일러스트 — 단행본 표지·웹툰 썸네일을 인쇄 해상도까지 생성 |
| `story-ip-pitch` | IP 사업화 — 2차 저작(드라마·영화·게임·굿즈) 피칭 문서·판권 제안서 |

### 한국어 마감 (2종)

| 스킬 | 역할 |
|------|------|
| `general-humanize-korean` | AI가 쓴 한국어의 "AI 티"를 제거하는 인문화 윤문 (의미·수치·인용 100% 보존, 변경률 30%/50% 가드) |
| `office-korean-spell-check` | 바른한글 기반 띄어쓰기·맞춤법·문법 최종 검수 |

## MCP 연동 1종

플러그인 루트 `.mcp.json`에 Higgsfield MCP 서버가 선언되어 있습니다.

| 서버 | 역할 | 인증 | 사용 스킬 |
|------|------|------|-----------|
| `higgsfield` | AI 이미지·영상 생성 (호스티드, `https://mcp.higgsfield.ai/mcp`) | Higgsfield 계정 토큰 (mcp.higgsfield.ai에서 발급) | `story-cover-art`, `story-webtoon-art`, `story-character-sheet`, `story-conti`, `story-ad-conti`, `story-previz` |

- 생성 작업은 크레딧이 소모되므로 각 스킬이 **사전 크레딧 고지 + 사용자 확인** 후에만 실행합니다
- MCP 미연결 시 프롬프트 온리 모드(생성 프롬프트만 산출)로 자동 전환됩니다

## 에이전트 2종

| 에이전트 | 등급 | 역할 |
|----------|------|------|
| `writer-director` | worker | 책 기획·원고, 웹툰·웹소설 에피소드, 시나리오, IP 피칭 산출물을 만드는 실무 에이전트. 목표 이해 → 계획 → book-*/story-* 스킬 선택 → 실행 → 검증의 에이전트 루프로 동작. 표절 금지·사실 앵커 보존·출판사/공모전 정보 출처 필수를 HARD 가드레일로 준수 |
| `manuscript-auditor` | read-only audit | 원고·제안서·IP 패키지를 회의적으로 검증하는 감사 에이전트 — 캐릭터·세계관·시점 일관성, 표절/AI 티 위험, 장르 관습 적합성, 제안서 완결성. 증거 기반 PASS/FAIL 판정만 반환하며 파일을 수정하지 않음 |

## 라이선스

LicenseRef-MoAI-NC-ND-1.0 · © modu-ai (email@mo.ai.kr)
