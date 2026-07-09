# moai-pm (PM) — 12명의 AI 직원을 부르는 진입점

> **PM**은 프로젝트를 처음 시작할 때 **어떤 AI 직원이 필요한지 판단해 팀을 꾸려 주는** 허브 플러그인입니다. 복잡한 설정 대신, "이런 일 할 거야"라고 말하면 알아서 적합한 AI 직원들로 연결해 줍니다.

---

## 두 가지 진입 모드

```
                        ┌──────────────┐
                        │  📋 PM 허브   │  /project
                        │  (라우팅만)   │  "무슨 일 할까?"
                        └──────┬───────┘
              ┌────────────────┴────────────────┐
              ▼                                 ▼
      /project --cowork                 /project --code
   ┌──────────────────────────┐      ┌─────────────────┐
   │ code 제외 모든 코워크 업무 │      │ 💻 코더 (moai)  │
   │ 🧑‍💼✍️📣🛒🗂️⚖️💰🤝🎓🎨    │      │ SPEC·DDD/TDD    │
   │ 지침 + 커스텀 에이전트 +   │      │ 개발환경 셋업    │
   │ 재귀적 자가 개선           │      └─────────────────┘
   └──────────────────────────┘
```

| 모드 | 커버리지 | 무엇을 하나요 |
|------|----------|---------------|
| `/project --cowork` | **code를 제외한 모든 클로드 코워크 프로젝트** | 프로젝트 인터뷰 → 설치된 AI 직원 인벤토리 스캔 → 스킬&에이전트 워크플로우 설계 → `CLAUDE.md` 생성 → `.claude/agents/` 커스텀 에이전트 생성 → **사용하면서 재귀적 자가 개선** (에이전트·CLAUDE.md가 개선 필요 신호를 보이면 자율적으로 개선) |
| `/project --code` | 개발 프로젝트 | 코더(moai) 개발환경 셋업 — MoAI-ADK 정본 스캐폴드, SPEC 워크플로우(DDD/TDD), 품질 게이트 |

---

## 12명의 AI 직원 ('MoAI-Claude, 모두의 클로드')

전부 `modu-ai/claude` 마켓플레이스 하나에서 설치합니다.

| AI 직원 | 플러그인 | 무엇을 하나요 |
|---------|---------|---------------|
| 🧑‍💼 코워커 | `moai-coworker` | 범용 비즈니스 실무 (전략·제안서·협상·고객대응) |
| ✍️ 작가 | `moai-writer` | 출판·웹툰·웹소설·시나리오·IP 창작 |
| 📣 마케터 | `moai-marketer` | 캠페인·콘텐츠·SNS·미디어 생성 |
| 🛒 셀러 | `moai-seller` | 이커머스 (스마트스토어·아임웹·카페24 MCP) |
| 🗂️ 사무관 | `moai-officer` | 오피스 문서·공공데이터·생산성 |
| ⚖️ 법무 담당 | `moai-lawyer` | 계약·법령·판례·특허 (korean-law MCP) |
| 💰 재무·세무 담당 | `moai-accountant` | 재무제표·결산·세금 (DART MCP) |
| 🤝 인사·채용 담당 | `moai-recruiter` | 채용·이력서·면접·평가 |
| 🎓 튜터 | `moai-tutor` | 커리큘럼·평가 문항·논문 |
| 🎨 디자이너 | `moai-designer` | 브랜드·디자인 시스템·Claude Design |
| 💻 코더 | `moai` | 개발 (SPEC DDD/TDD·품질 게이트, `/moai`) |
| 📋 PM | `moai-pm` (본 플러그인) | 위 11명 중 **누가 필요한지 판단해 연결** |

PM은 직접 일하지 않습니다. **누가 이 일에 맞는지 찾아 팀을 꾸리는 안내자** 역할만 합니다.

---

## 설치

### ① 마켓플레이스 등록 (최초 1회만)

'MoAI-Claude, 모두의 클로드' 12명의 AI 직원은 `modu-ai/claude` 마켓플레이스 하나에 들어있습니다. Claude Code(또는 Desktop)에서 한 번만 등록하면 됩니다:

    /plugin marketplace add modu-ai/claude

### ② 플러그인 추가

**가장 쉬운 방법** — `/plugin`이라고 치면 나오는 창에서 **"Browse Plugins"**을 누르고 원하는 직원을 선택하세요.

**직접 명령으로** 설치하려면:

    /plugin install moai-pm@moai-claude            # PM 허브 (필수)
    /plugin install moai-coworker@moai-claude      # 범용 실무 코어 (권장)
    # 필요한 전문가 직원 추가: moai-writer / moai-marketer / moai-seller / moai-officer /
    # moai-lawyer / moai-accountant / moai-recruiter / moai-tutor / moai-designer / moai(코더)

> 처음엔 PM + 코워커만 설치해도 충분합니다. 나중에 다른 직원이 필요해지면 셋업 중 **Gap Detection**이 감지해 **"이 직원을 설치해 주세요"**라고 안내한 뒤, 설치 완료 시 `/project resume`으로 이어서 진행합니다.

---

## 사용법

### 처음 시작

```
/project
```

PM이 먼저 인사하고 무엇을 할지 묻습니다. "온라인 클래스 런칭 준비할 거야"처럼 답하면 PM이 `--cowork` 셋업으로 진행합니다. 개발 프로젝트면 `--code`로 분기합니다.

### 커맨드

| 커맨드 | 동작 |
|--------|------|
| `/project` | 의도 감지 후 2-모드 분기 (기본) |
| `/project --cowork` | 코워크 프로젝트 셋업 (code 외 전부) |
| `/project --code` | 코더 개발환경 셋업 |
| `/project resume` | 플러그인 설치 후 이어서 진행 |
| `/project evolve` | 재귀적 자가 개선 수동 발동 |
| `/project catalog` | 12-plugin·스킬 카탈로그 |
| `/project status` | 현재 설정 상태 |
| `/project apikey` | API 키 관리 |
| `/project doctor` | 환경 진단 |
| `/project feedback` | GitHub 이슈 등록 |

### 재귀적 자가 개선 (--cowork 셋업 프로젝트)

셋업이 끝난 뒤에도 PM의 역할은 끝나지 않습니다. 사용 중 아래 신호가 감지되면 에이전트와 CLAUDE.md를 **자율적으로 개선**합니다:

- 같은 유형의 수정 요청이 반복될 때 (톤·형식 불일치)
- 에이전트가 같은 단계에서 반복 실패할 때
- 플러그인 설치·제거로 워크플로우 표가 실제와 어긋날 때
- 사용자가 직접 요청할 때 (`/project evolve`)

개선은 최소 diff 단위로만 이루어지고, 변경 요지를 1-3줄로 보고한 뒤 적용하며, 이력은 CLAUDE.md 말미에 기록됩니다.

---

## 산출물

| 파일 | 내용 |
|------|------|
| `./CLAUDE.md` | 프로젝트 지침 (≤200라인) — 워크플로우 표 + HARD 규칙 + evolution-log |
| `./.claude/agents/*.md` | 프로젝트 특화 커스텀 에이전트 (자가 개선 대상) |
| `./.moai/skill-profile.yaml` | 스킬-선택 CONFIG |
| `./.moai/credentials.env` | API 키 (프로젝트 격리) |

---

## 라이선스

LicenseRef-MoAI-NC-ND-1.0 · © modu-ai (email@mo.ai.kr)
