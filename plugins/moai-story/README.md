# 스토리 크리에이터 (moai-story)

스토리/IP 창작 전담 AI 직원입니다. 웹툰·웹소설·시나리오·콘티·표지·캐릭터 시트·IP 사업화(story-* 13종) 스킬과 Higgsfield 이미지·영상 MCP 연동을 하나의 플러그인으로 제공합니다. 슬래시 명령을 외울 필요 없이 자연어로 요청하면 매칭되는 스킬이 자동 호출됩니다.

> **분리 안내**: 본 플러그인의 스토리 스킬들은 `moai-writer`에서 분리되었습니다(출판 book-* 스킬은 moai-writer에 잔류). 신규 호출은 `moai-story:<스킬명>` 네임스페이스를 사용하세요.

**이런 분께 추천**: 웹툰/웹소설 창작자 · 시나리오 작가 · IP 콘텐츠 기획자

## 설치

```
claude plugin marketplace add modu-ai/moai-cowork
claude plugin install moai-story@moai-cowork
```

또는 Claude Code 세션 안에서:

```
/plugin marketplace add modu-ai/moai-cowork
/plugin install moai-story
```

## 스킬 13종

호출 형식: `/moai-story:<스킬명>` — 예: `/moai-story:story-webtoon-episode`. 자연어 요청("웹툰 회차 대본 써줘")으로도 자동 매칭됩니다.

### 스토리·IP (story-* 13종)

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
| `story-director` | worker | 웹툰·웹소설 에피소드, 시나리오, 콘티/프리비즈, 표지, IP 피칭 산출물을 만드는 실무 에이전트. 목표 이해 → 계획 → story-* 스킬 선택 → 실행 → 검증의 에이전트 루프로 동작. 표절 금지·캐릭터/Soul-ID 연속성 보존·플랫폼/제작사 정보 출처 필수·Higgsfield 크레딧 사전 고지를 HARD 가드레일로 준수 |
| `story-continuity-auditor` | read-only audit | 스토리 산출물을 회의적으로 검증하는 감사 에이전트 — 캐릭터·플롯·설정 연속성(Soul-ID 포함), 플랫폼 포맷 적합성, 표절/AI 티 위험, IP 권리/피칭 완결성. 증거 기반 PASS/FAIL 판정만 반환하며 파일을 수정하지 않음 |

## 라이선스

LicenseRef-MoAI-NC-ND-1.0 · © modu-ai (email@mo.ai.kr)
