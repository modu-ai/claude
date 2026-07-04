---
title: "moai-code 플러그인"
weight: 40
description: "MoAI-ADK SPEC plan/run/sync 개발 방법론 무설치 플러그인 — moai CLI 없이 Claude Code/Desktop에서 DDD/TDD·품질 게이트·문서 동기화. 13개 명령·7개 에이전트·28개 스킬."
geekdocBreadcrumb: true
geekdocCollapseSection: false
ia_in_scope: true
aliases:
  - /plugins/code
---

## moai CLI 없이 /moai로 개발하기, moai-code

`moai-code`는 **MoAI-ADK의 개발 방법론(SPEC plan → run → sync)을 Claude Code와 Claude Desktop 안에서 그대로 쓸 수 있게 만든 무설치 플러그인**입니다. 원래 MoAI는 `moai`라는 CLI 바이너리를 통해 실행되는데, 이 플러그인은 그 바이너리 없이도 — 즉 Claude Code 익스텐션 설치만으로 — `/moai plan`, `/moai run`, `/moai sync` 명령을 그대로 부를 수 있게 해 줍니다. 내부적으로는 13개의 슬래시 명령, 7개의 위임용 에이전트, 28개의 도메인 스킬로 구성되어 있고, 마켓플레이스 기준 이름은 `moai`, 버전은 3.0.0입니다.

이 플러그인의 차이점은 **개별 기능이 아니라 개발 사이클 전체**를 묶어 놓는다는 점입니다. 일반적인 코딩 보조 플러그인이 "코드 리뷰 해 줘", "테스트 만들어 줘" 같은 단건 작업을 처리한다면, moai-code는 [SPEC 문서를 먼저 쓰고 → 그 SPEC에 맞춰 구현하고 → 산출물을 문서로 동기화하는](/cli/) 전체 흐름을 하나의 워크플로로 다룹니다. 그래서 비개발자도 "이 기능을 만들고 싶다"고 말하면, `/moai plan`부터 시작해 명확한 요구명세서를 거쳐 구현까지 도달할 수 있습니다. SPEC-First DDD/TDD가 단순한 개념이 아니라, 실제 파일(`.moai/specs/SPEC-XXX/`)에 기록되는 산출물이 된다는 것이 핵심입니다.

## 설치 흐름 한눈에 보기

```mermaid
flowchart LR
    A["Claude Code<br/>또는 Claude Desktop"] --> B["플러그인 추가<br/>moai (버전 3.0.0)"]
    B --> C["무설치 — moai CLI<br/>불필요"]
    C --> D["/moai plan 으로<br/>SPEC 작성"]
    D --> E["/moai run 으로<br/>구현 (DDD/TDD)"]
    E --> F["/moai sync 으로<br/>문서 동기화"]
    F --> G[".moai/specs/SPEC-XXX/<br/>plan+run+sync 산출물"]

    A -. 같은 엔진 .- H["터미널 친화적 사용자는<br/>moai CLI 바이너리"]
    H -. I["/cli/ 축으로 .- D

    style A fill:#eaeaea,stroke:#6e6e6e,color:#09110f
    style B fill:#fbf0dc,stroke:#c47b2a,color:#09110f
    style C fill:#f5dcd7,stroke:#c44a3a,color:#09110f
    style D fill:#dceee9,stroke:#2a8a8c,color:#09110f
    style E fill:#dceee9,stroke:#2a8a8c,color:#09110f
    style F fill:#dceee9,stroke:#2a8a8c,color:#09110f
    style G fill:#788C5D,stroke:#5F6F4A,color:#FFFFFF
    style H fill:#e6f0ef,stroke:#144a46,color:#09110f
```

설치는 Claude Code의 확장 메뉴나 Cowork 플러그인 마켓플레이스에서 `moai`를 검색해 추가하면 됩니다. 별도의 `moai` 바이너리 설치가 필요 없는 것이 이 플러그인의 핵심 가치입니다 — 이미 Claude Code 환경을 쓰고 있다면 추가 인프라 없이 `/moai plan` 명령부터 바로 시작할 수 있습니다. 터미널을 선호하는 개발자라면 `/cli/` 축에서 `moai` CLI 바이너리를 직접 설치하는 동선도 가능하고, 두 경로 모두 같은 `.moai/specs/` 산출물을 만듭니다.

## 대표 스킬·명령 Top 5

moai-code는 스킬뿐 아니라 명령(slash command)과 에이전트(sub-agent)도 함께 제공합니다. 그래서 Top 5는 "사용자가 가장 자주 부르는 진입점" 기준으로 뽑았습니다.

| 진입점 | 종류 | 하는 일 | 자주 같이 쓰는 |
|---|---|---|---|
| **/moai plan** | 명령 | SPEC 문서 작성 (GEARS 형식 요구명세 + 인수조건 + 실행계획) | `/moai run`, `manager-spec` 에이전트 |
| **/moai run** | 명령 | SPEC에 맞춰 구현 (DDD ANALYZE-PRESERVE-IMPROVE 또는 TDD RED-GREEN-REFACTOR) | `/moai sync`, `manager-develop` 에이전트 |
| **/moai sync** | 명령 | 산출물을 README·CHANGELOG·codemaps로 동기화 + PR 생성 | `manager-docs`, `manager-git` 에이전트 |
| **manager-spec** | 에이전트 | plan-phase 산출물(spec.md/plan.md/acceptance.md) 작성 전담 | `plan-auditor` |
| **moai-foundation-core** | 스킬 | TRUST 5·SPEC-First DDD·토큰 최적화 기반 원칙 레퍼런스 | `moai-workflow-tdd`, `moai-workflow-ddd` |

처음에는 `/moai plan`으로 작은 SPEC 하나를 만들어 보는 것을 권합니다. 예를 들어 "로그인 페이지에 소셜 로그인 추가" 정도의 작은 기능으로 시작하면, plan → run → sync 사이클이 한 바퀴 도는 데 필요한 산출물 구조(`.moai/specs/SPEC-XXX/`)가 감이 잡힙니다.

## 전체 인덱스 — 명령 13개 + 에이전트 7개 + 스킬 28개

moai-code는 세 종류의 구성 요소를 함께 제공합니다. **명령**은 사용자가 직접 부르는 진입점, **에이전트**는 명령 안에서 위임되는 전문가, **스킬**은 에이전트가 참조하는 도메인 지식 묶음입니다.

### 명령 (13) — /moai 서브명령

- **/moai plan** — SPEC 문서 작성 (plan-phase).
- **/moai run** — 구현 실행 (run-phase, DDD 또는 TDD).
- **/moai sync** — 산출물 동기화 + PR 생성 (sync-phase).
- **/moai project** — 프로젝트 문서 생성 (product/structure/tech.md, codemaps/).
- **/moai loop** — 반복적 품질 개선 (Ralph Engine).
- **/moai fix** — LSP/린트/타입 에러 자동 수정.
- **/moai review** — 코드 리뷰 + @MX 태그 컴플라이언스.
- **/moai gate** — 사전 커밋 품질 게이트 (린트+포맷+타입+테스트 병렬).
- **/moai clean** — 죽은 코드 식별·제거 (테스트 검증과 함께).
- **/moai codemaps** — 코드베이스 아키텍처 문서 생성.
- **/moai mx** — @MX 코드 주석 자동 추가.
- **/moai harness** — 하네스 학습/빌더 관리.
- **/moai feedback** — 모두의AI 도구 저장소에 피드백/이슈 등록.

### 에이전트 (7) — 위임용 서브에이전트

- **manager-spec** — plan-phase 산출물 작성.
- **manager-develop** — run-phase 구현 (cycle_type: ddd/tdd/autofix).
- **manager-docs** — sync-phase 문서화 + 프론트매터 전환.
- **manager-git** — Tier 기반 PR 라우팅 + Late-Branch 종료.
- **plan-auditor** — plan-phase 독립 감사 (편향 방지).
- **sync-auditor** — sync-phase 4차원 품질 평점 (Functionality/Security/Craft/Consistency).
- **builder-harness** — 동적 프로젝트별 하네스 전문가 생성.

### 스킬 (28) — 도메인·워크플로 지식

- **기반 원칙 (5)** — `moai-foundation-core` (TRUST 5/SPEC-First DDD), `moai-foundation-cc` (Claude Code 저작), `moai-foundation-quality` (품질 게이트), `moai-foundation-thinking` (사고 프레임워크), `moai-meta-harness` (레거시 하네스 리다이렉트).
- **워크플로 (8)** — `moai-workflow-spec` (SPEC/GEARS), `moai-workflow-tdd`, `moai-workflow-ddd`, `moai-workflow-testing`, `moai-workflow-project`, `moai-workflow-loop` (Ralph Engine), `moai-workflow-ci-loop`, `moai-workflow-worktree`.
- **도메인 (5)** — `moai-domain-backend`, `moai-domain-frontend`, `moai-domain-database`, `moai-domain-html-report`, `moai-domain-humanize`.
- **보안·공급망 레퍼런스 (6)** — `moai-ref-owasp-checklist`, `moai-ref-llm-security`, `moai-ref-api-patterns`, `moai-ref-secops`, `moai-ref-supply-chain`, `moai-ref-react-patterns`, `moai-ref-testing-pyramid`, `moai-ref-git-workflow`.
- **하네스 (1)** — `moai-harness-learner`.
- **통합 진입점 (1)** — `moai` (단일 진입점 스킬).
- **도구 (1)** — `moai-domain-html-report`.

## 레시피 — 명령·에이전트를 엮어서 쓰는 흐름

### 레시피 1 — SPEC-First 한 사이클 (기본)

`/moai plan "기능 설명"` (SPEC 작성, manager-spec 위임) → (plan-auditor 독립 감사) → `/moai run SPEC-XXX` (구현, manager-develop에 cycle_type=tdd 위임) → `/moai sync SPEC-XXX` (문서 동기화 + PR).

### 레시피 2 — 기존 코드 DDD 리팩토링

`/moai plan "리팩토링 대상"` (SPEC 작성, 개발 모드 DDD 명시) → `/moai run SPEC-XXX` (ANALYZE-PRESERVE-IMPROVE 사이클) → `/moai sync SPEC-XXX`. DDD는 행동 보존을 전제로 한 리팩토링 사이클이므로 기존 테스트가 깨지지 않는 것이 핵심입니다.

### 레시피 3 — 품질 게이트 병렬 점검

`/moai gate` (린트+포맷+타입+테스트 병렬 실행) → 실패 시 `/moai fix` (자동 수정) → 재실행. CI 직전에 가볍게 품질 바닥을 잡을 때 씁니다.

## 다음 단계

- **[CLI (개발자용) 축](/cli/)** — moai CLI 바이너리로 넘어가는 심화 경로. 무설치 플러그인에서 시작해 CLI로 확장.
- **[moai-cowork 플러그인](/plugins/cowork/)** — 개발 산출물(README·문서)을 한국 실무 문서로 마무리할 때.
- **[SPEC 시스템 개념](/cli/concepts/)** — SPEC이 왜 필요한지, plan-run-sync가 어떤 문제를 푸는지.

---

### Sources

- moai-code 플러그인 소스: [`/plugins/moai-code/`](https://github.com/modu-ai/claude.mo.ai.kr/tree/main/plugins/moai-code) (명령 13·에이전트 7·스킬 28 포함)
- 마켓플레이스 진실 원본: [`/plugins/moai-code/.claude-plugin/plugin.json`](https://github.com/modu-ai/claude.mo.ai.kr/blob/main/plugins/moai-code/.claude-plugin/plugin.json) (`name: moai`, `displayName: MoAI Code`, `version: 3.0.0`)
- MoAI-ADK CLI 명령어 원본 문서: <https://adk.mo.ai.kr/ko/workflow-commands/>
- SPEC-First DDD 안내: [CLI 축 핵심 개념](/cli/concepts/)
- Claude Code 공식 문서 — sub-agents: <https://code.claude.com/docs/en/sub-agents>
