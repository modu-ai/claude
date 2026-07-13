# moai-pm (PM) — 18개 AI 직원을 부르는 진입점

> **PM**은 프로젝트를 시작할 때 **어떤 AI 직원이 필요한지 판단해 팀을 꾸려 주는** 허브 플러그인입니다. 이제 두 개의 전담 스킬로 나뉘어, 각자 자신의 영역을 더 깊이 담당합니다: **goose**(개발 외 모든 Claude Cowork 업무)와 **moai**(개발 프로젝트 초기화).

---

## 두 개의 스킬

```
                        ┌───────────────────────┐
                        │  이번에 뭘 할 건가요?   │
                        └───────────┬───────────┘
              ┌────────────────────┴────────────────────┐
              ▼                                          ▼
      /goose --project                          /moai --project
   ┌──────────────────────────┐            ┌──────────────────────────┐
   │ 🪿 goose                 │            │ 💻 moai                 │
   │ code를 제외한 모든        │            │ 개발-프로젝트 초기화     │
   │ Claude Cowork(Desktop)    │            │ (moai-adk v3.0 철학,     │
   │ 업무 — 지침 + 커스텀      │            │ SPEC plan/run/sync,      │
   │ 에이전트 + 재귀적 자가    │            │ TRUST 5, DDD/TDD)        │
   │ 개선                      │            │                          │
   └──────────────────────────┘            └──────────────────────────┘
```

| 스킬 | 커맨드 | 런타임 전제 | 무엇을 하나요 |
|------|--------|-------------|---------------|
| **goose** | `/goose --project` | Claude Cowork(Desktop) | 소크라테스 인터뷰 → 설치된 AI 직원 인벤토리 스캔 → **프로젝트 전용 커스텀 에이전트·스킬 체인 설계** → `CLAUDE.md`(≤200라인) + `.claude/agents/` + `.moai/` 스캐폴드 생성 → **사용하면서 재귀적 자가 개선** |
| **moai** | `/moai --project` | Claude Code | 소크라테스 인터뷰 + 스택 감지 → `CLAUDE.md`·`.claude/agents/`·`.claude/skills/`·`.claude/settings.json`·hooks·`.mcp.json` 생성 → 코더 플러그인 설치 시 실행 라우팅, 미설치 시 가이던스 전용 |

> **명령 표면 주의**: `/moai --project`(플래그, moai-pm 소유)와 `/moai project`(공백 서브커맨드, 코더 플러그인 소유 — `product.md`/`structure.md`/`tech.md` 생성)는 **서로 다른 진입점**입니다. `--project` 플래그가 `project` 서브커맨드를 가리거나 대체하지 않습니다.

---

## `/project` 명령 — 모드 라우터

`/moai-pm:project [--cowork|--code] <자연어 지시>` 한 줄로 프로젝트 폴더 초기화를 시작합니다.

| 모드 | 상태 | 동작 |
|------|------|------|
| `--cowork` (기본, 플래그 생략 가능) | ✅ 사용 가능 | **goose 스킬** 발동 — 소크라테스 인터뷰 → 직원 인벤토리 스캔 → `CLAUDE.md` + `.claude/agents/` + `.moai/` 스캐폴드 생성 |
| `--code` | 🚧 개발 중 (미배포) | 추후 **moai 스킬**로 라우팅되어 `moai init`과 동일한 개발 프로젝트 초기화를 수행할 예정. 현재는 안내 메시지만 출력 |

---

## 18개 AI 직원 ('MoAI-Claude, 모두의 클로드')

전부 `modu-ai/claude` 마켓플레이스 하나에서 설치합니다. 정확한 로스터·스킬 수는 마켓플레이스 카탈로그(`/goose catalog`)가 정본입니다 — 아래는 역할 요약입니다.

| AI 직원 | 플러그인 | 무엇을 하나요 | 진입 스킬 |
|---------|---------|---------------|-----------|
| 🧑‍💼 코워커 | `moai-coworker` | 범용 비즈니스 실무 + 라이프스타일 | goose |
| ✍️ 작가 | `moai-writer` | 출판 기획·집필(book-*) | goose |
| 🎬 스토리 크리에이터 | `moai-story` | 웹툰·웹소설·시나리오·IP(story-*) | goose |
| 📣 마케터 | `moai-marketer` | 캠페인·콘텐츠 | goose |
| 🎨 미디어 크리에이터 | `moai-media` | 이미지·영상·오디오 생성 | goose |
| 🛒 셀러 | `moai-seller` | 이커머스(스마트스토어·아임웹·카페24 MCP) | goose |
| 🗂️ 사무관 | `moai-officer` | 오피스 문서 | goose |
| 📊 데이터 애널리스트 | `moai-analyst` | 공공데이터·데이터 시각화 | goose |
| ⚖️ 법무 담당 | `moai-lawyer` | 계약·법령·판례·특허 | goose |
| 💰 재무·세무 담당 | `moai-accountant` | 재무제표·결산·세금 | goose |
| 🤝 인사·채용 담당 | `moai-recruiter` | 채용·이력서·면접·평가 | goose |
| 🎧 CS매니저 | `moai-cs` | 고객지원·CRM·VOC 분석 | goose |
| 🧭 컨설턴트 | `moai-consultant` | 사업계획·시장분석·경영 진단 | goose |
| 🎯 커리어코치 | `moai-career` | 이력서·면접·이직(구직자 편) | goose |
| 🎓 튜터 | `moai-tutor` | 커리큘럼·평가·논문 | goose |
| 🎨 디자이너 | `moai-designer` | 브랜드·디자인 시스템·Claude Design | goose |
| 💻 코더 | `moai` | 개발(SPEC DDD/TDD·품질 게이트) | moai |
| 📋 PM | `moai-pm`(본 플러그인) | goose + moai 두 어드바이저 스킬 제공 | — |

PM은 직접 일하지 않습니다. **누가 이 일에 맞는지 찾아 팀을 꾸리는 안내자** 역할만 합니다.

---

## 설치

### ① 마켓플레이스 등록 (최초 1회만)

'MoAI-Claude, 모두의 클로드' 18개 AI 직원은 `modu-ai/claude` 마켓플레이스 하나에 들어있습니다:

    /plugin marketplace add modu-ai/claude

### ② 플러그인 추가

**가장 쉬운 방법** — `/plugin`이라고 치면 나오는 창에서 **"Browse Plugins"**을 누르고 원하는 직원을 선택하세요.

**직접 명령으로** 설치하려면:

    /plugin install moai-pm@moai-claude            # PM 허브 (필수)
    /plugin install moai-coworker@moai-claude       # 범용 실무 코어 (권장, goose 분기)
    /plugin install moai@moai-claude                # 코더 개발환경 (moai 분기)
    # 필요한 전문가 직원 추가: moai-writer / moai-story / moai-marketer / moai-media /
    # moai-seller / moai-officer / moai-analyst / moai-lawyer / moai-accountant /
    # moai-recruiter / moai-cs / moai-consultant / moai-career / moai-tutor / moai-designer

> 처음엔 PM + 코워커만 설치해도 충분합니다. 나중에 다른 직원이 필요해지면 셋업 중 **Gap Detection**이 감지해 설치를 안내한 뒤, 완료 시 `/goose resume`(또는 `/moai resume`)으로 이어서 진행합니다.

---

## 사용법

### 개발 외 업무 (goose)

```
/goose --project
```

goose가 먼저 인사하고 무엇을 할지 묻습니다. "온라인 클래스 런칭 준비할 거야"처럼 답하면 프로젝트 전용 커스텀 에이전트와 스킬 체인을 설계해 `CLAUDE.md`를 생성합니다.

### 개발 프로젝트 (moai)

```
/moai --project
```

moai가 프로젝트 유형·기술 스택을 인터뷰/감지한 뒤 MoAI-ADK 3.0 정본 baseline을 설치합니다.

### 커맨드

| 커맨드 | 동작 |
|--------|------|
| `/goose --project` | goose 진입 — code 외 전부 |
| `/moai --project` | moai 진입 — 개발 프로젝트 초기화 |
| `/goose resume` / `/moai resume` | 플러그인 설치 후 이어서 진행 |
| `/project evolve` | goose 재귀적 자가 개선 수동 발동(레거시 단일-슬래시 형태 유지) |
| `/goose catalog` | 18-plugin·스킬 카탈로그 |
| `/goose status` / `/moai status` | 현재 설정 상태 |
| `/goose apikey` / `/moai apikey` | API 키 관리 |
| `/goose doctor` / `/moai doctor` | 환경 진단(각 런타임에 맞춰) |

### 재귀적 자가 개선 (goose 셋업 프로젝트)

셋업이 끝난 뒤에도 goose의 역할은 끝나지 않습니다. 사용 중 아래 신호가 감지되면 에이전트와 `CLAUDE.md`를 **자율적으로 개선**합니다:

- 같은 유형의 수정 요청이 2회 이상 반복될 때(톤·형식 불일치)
- 스킬 체인이 반복적으로 같은 단계에서 실패·우회할 때
- 플러그인 설치·제거로 인벤토리가 실제와 어긋날 때(inventory drift)
- 사용자가 직접 요청할 때(`/project evolve`)

개선은 최소 diff(최대 3개 파일) 단위로만 이루어지고, 변경 요지를 1-3줄로 보고한 뒤 적용하며, 이력은 `CLAUDE.md` 말미 `<!-- evolution-log -->`에 기록됩니다. 자가 개선은 `CLAUDE.md`와 `.claude/agents/`만 수정합니다.

---

## 산출물

### goose

| 파일 | 내용 |
|------|------|
| `./CLAUDE.md` | 프로젝트 지침(≤200라인) — 워크플로우 표 + 8개 HARD 규칙 + evolution-log |
| `./.claude/agents/*.md` | 프로젝트 전용 커스텀 에이전트(자가 개선 대상) |
| `./.moai/config.json` | 플러그인·커넥터·API 키 참조 |
| `./.moai/credentials.env` | API 키 안내(프로젝트 격리, GUIDANCE 전용 — 실제 값은 기록하지 않음) |

### moai

| 파일 | 내용 |
|------|------|
| `./CLAUDE.md` | MoAI-ADK 3.0 정본 오케스트레이터 지침(코더 정본 소스, PM 공통 tmpl 미적용) |
| `./.claude/agents/`, `./.claude/skills/` | 코더 정본 8-에이전트 + 프로젝트 특화 스킬 |
| `./.claude/settings.json` | 권한 allowlist + hooks 배선 |
| `./.mcp.json` | 서베이-선택된 MCP 서버(자격증명 미포함) |

---

## 라이선스

LicenseRef-MoAI-NC-ND-1.0 · © modu-ai (email@mo.ai.kr)
