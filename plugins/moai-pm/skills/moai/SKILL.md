---
name: moai
description: |
  **개발-프로젝트 초기화 어드바이저** — moai-adk v3.0 철학(SPEC plan/run/sync 워크플로우, TRUST 5 품질, DDD/TDD)을 담당한다.
  `/moai --project <지시>`로 진입하며, Claude Code 런타임을 전제로 소크라테스 인터뷰 + 스택 감지 후
  `CLAUDE.md`·`.claude/agents/`·`.claude/skills/`·`.claude/settings.json`·hooks 스크립트·`.mcp.json`을 생성한다.
  코더 플러그인(`moai`)이 설치되어 있으면 실행을 그쪽으로 라우팅하고, 없으면 임베디드 카탈로그 요약으로
  가이던스 전용 축소 모드로 동작한다.

  다음과 같은 요청 시 반드시 이 스킬을 사용하세요:
  - "개발 프로젝트 시작", "개발환경 셋업", "MoAI-ADK 세팅", "SPEC 워크플로우 잡아줘"
  - "/moai --project ...", "/moai resume", "/moai catalog", "/moai status", "/moai apikey", "/moai doctor"
  - 개발·코딩·SPEC·DDD/TDD 관련 자연어 요청이 들어왔을 때

  이 스킬은 코더 플러그인(`plugins/moai`)의 `/moai project` 서브커맨드(product/structure/tech.md 생성)와는
  **다른 진입점**이다 — 아래 §Namespace & Routing 참조. 글로벌 프로필을 재질문하지 않는다.
user-invocable: true
version: "0.1.0"
---
<!-- moai-pm moai v0.1.0 · 18-plugin 패밀리(v6.2) · 개발-프로젝트 초기화 어드바이저 (project 스킬 대체, SPEC-MOC-PM-ADVISORS-001) -->

# moai — 개발-프로젝트 초기화 어드바이저

사용자는 어떤 개발 프로젝트를 시작할지 말해주면 됩니다. moai 스킬이 소크라테스 인터뷰와 스택 감지로 맥락을 파악한 뒤, moai-adk v3.0 정본 baseline(`CLAUDE.md`·`.claude/`·`.moai/`·`.mcp.json`)을 설치·구성합니다.

## 개요

moai 스킬은 **Claude Code 런타임**을 전제하는 개발-프로젝트 초기화 어드바이저다. `conversation_language`로 대화하며, 모든 확인은 `AskUserQuestion`로만 수행한다. 코더 플러그인(`plugins/moai`)이 설치되어 있으면 초기화 산출물 생성 후 실행을 그쪽으로 라우팅하고, 없으면 가이던스 전용(guidance-only) 축소 모드로 동작한다(§Namespace & Routing).

**개요 안내 (첫 만남)**: 사용자가 `/moai --project`로 처음 진입하면, 인터뷰에 들어가기 전에 다음을 먼저 출력한다. 재진입 시 생략한다.

> 안녕하세요, 저는 **moai**예요. `moai` CLI 설치 없이 Claude Code에서 SPEC 기반 개발(PLAN › RUN › SYNC)을 준비해 드리는 동료입니다. 어떤 개발 프로젝트를 시작할까요? 언어·프레임워크를 말씀해 주시면 맞춰 셋업해 드릴게요.

---

## Socratic Interview & Stack Detection

`/moai --project` 진입 시, 생성을 시작하기 **전에** 소크라테스 인터뷰와 스택 감지를 함께 수행한다. 글로벌 프로필(이름·회사·역할)은 재질문하지 않는다.

**맥락 등급 (A/B/C, goose와 동일 모델)**: A등급(기존 `CLAUDE.md`/`product.md`/`tech.md`에서 즉시 획득) → 질문 없이 사용. B등급(핵심 — 프로젝트 유형·기술 스택·문서 언어·품질 게이트 깊이) → Phase 1 인터뷰 + 필요 시 `AskUserQuestion` 보강. C등급(보강 — 팀 규모·CI 환경 등) → 심화 인터뷰(텍스트 대화, 최대 2질문).

**인터뷰 수집 항목**:

| 질문 영역 | 수집 내용 |
|---|---|
| 프로젝트 유형 | 웹 앱·모바일·CLI·라이브러리·ML 프로젝트 |
| 기술 스택 | 언어·프레임워크·DB·주요 의존성(자동 감지 + 확인) |
| 문서 언어 | ko·en·ja·zh |
| 품질 게이트 깊이 | minimal·standard·thorough(harness level) |
| 개발 방법론 | DDD(레거시 리팩토링) / TDD(신규 기능) 자동 선택 기준 |

**스택 자동 감지**: 프로젝트 루트의 매니페스트(`package.json`/`go.mod`/`pyproject.toml`/`Cargo.toml` 등)를 스캔해 언어·프레임워크 후보를 도출하고, 인터뷰에서는 감지 결과를 확인만 받는다(재입력 요구 금지).

**재개(resume) 인터뷰**: 기존 `CLAUDE.md`/`.moai/config/sections/*.yaml`을 먼저 읽어 이미 확립된 맥락을 재사용한다.

**재진입 확인 (S3)**: 대상 프로젝트에 이미 `CLAUDE.md`·`.claude/`·`.moai/`가 존재하면, 기존 산출물을 덮어쓰기 전에 `AskUserQuestion`으로 명시적 확인을 받는다(옵션: 재생성 / 부분 갱신 / 취소). 침묵 덮어쓰기는 금지한다.

---

## Generation Targets

Phase 확인 이후 moai 스킬은 대상 프로젝트에 다음을 생성한다(REQ-M-003):

1. **`CLAUDE.md`** — moai-adk v3.0 정본 오케스트레이터 지침. PM 공통 `CLAUDE.md.tmpl`(코워커 체인용)은 이 분기에 **적용하지 않는다**(두-템플릿 분리 — §Two-Template Separation). 코더 플러그인 설치 시 `moai:moai-workflow-project` 정본 templates가 유일한 소스다.
2. **`.claude/agents`** — 8개 retained 에이전트 정의(코더 정본 패리티).
3. **`.claude/skills`** — 프로젝트 특화 스킬(필요 시).
4. **`settings.json`** — `.claude/settings.json`: 권한 allowlist + hooks 배선.
5. **hooks** — 품질 게이트·fact-force·status-transition 훅 스크립트(Claude Code 런타임 전제 — §Claude Code Runtime Assumption).
6. **`.mcp.json`** — SPEC-MOC-CODER-LSP-MCP-001 카탈로그에서 서베이-선택된 서버로만 구성(자격증명은 절대 인라인하지 않는다 — `.env` 가이던스만).

부가 산출물: `product.md`·`structure.md`·`tech.md`(`moai-workflow-project` doc-templates), `.moai/config/sections/*.yaml`, `.moai/specs/`(SPEC 워크플로우 디렉터리).

---

## LSP Presence Check

`/moai --project` 생성 단계에서 LSP 서버 설치 여부를 점검하고 언어별 설치 안내를 표시한다. 카탈로그와 설치 안내 콘텐츠는 SPEC-MOC-CODER-LSP-MCP-001이 소유하며, 이 스킬은 그 결과를 **소비만** 한다(전체 표를 중복 유지하지 않는다).

- 감지 대상: 프로젝트 스택에서 도출된 언어별 LSP 서버(`plugins/moai/.lsp.json` 5개 언어 플랫 키 baseline — go/python/rust/swift/typescript, 코더 정본 참조).
- 미설치 시: 언어별 설치 명령을 안내하고, 초기화 자체는 차단하지 않는다(advisory-only).
- LSP 설정 파일 자체는 코더 플러그인이 소유한다 — 이 스킬은 존재 여부만 확인하고 값을 복제하지 않는다.

---

## MCP Survey

`.mcp.json` 생성 전에 사용 가능한 MCP 서버를 서베이한다.

- **카탈로그-드리븐 선택**: `plugins/moai/references/dev-mcp-catalog.json`(SPEC-MOC-CODER-LSP-MCP-001 소유, `$schema_version` 필드로 버전 확인)을 읽어 서버 후보를 제시하고 `AskUserQuestion`으로 선택받는다.
- **`entry_type: "guidance-only"` 서버 제외**: 카탈로그 항목 중 `entry_type`이 `"guidance-only"`인 서버(예: 브라우저 자동화 확장)는 `.mcp.json` 서버 항목을 생성하지 않는다 — 안내 문구만 표시한다.
- **자격증명**: 카탈로그는 `.env` 가이던스만 제공한다. 생성되는 `.mcp.json`에 자격증명 값을 절대 인라인하지 않는다.
- **카탈로그 부재/파싱 실패**: 임베디드 폴백 요약(`references/mcp-fallback-summary.md`)으로 축소하고, 초기화를 하드 실패시키지 않는다.

---

## Namespace & Routing

- **`moai-pm:moai`**(본 스킬) = Desktop-side 초기화 어드바이저. **`moai:moai`**(코더 플러그인) = 실행.
- **Where** 코더 플러그인이 설치되어 있으면 → `moai-pm:moai`는 초기화 산출물 생성 후 실행을 코더 플러그인으로 라우팅한다.
- **Where** 코더 플러그인이 부재하면 → 가이던스 전용 축소 모드: 생성된 초기화 산출물 + 설치 안내 + 임베디드 카탈로그 fallback 요약(`references/mcp-fallback-summary.md`). 이 fallback 분기는 실행 라우팅을 **절대 시도하지 않는다** — 문서·안내만 제공한다.
- 단축형 `/moai` 런타임 디스패치 순서는 플랫폼 정의 사항으로, 본 스킬은 명시적 네임스페이스(`moai-pm:moai` / `moai:moai`)로 충돌을 해소한다.

### 커맨드 표면 명확화 — `/moai project` vs `/moai --project`

두 표면이 `moai`+`project` 토큰을 공유하지만 서로 다른 진입점이다:

| 표면 | 형태 | 소유 | 의미 | 근거 |
|---|---|---|---|---|
| `/moai project` | 서브커맨드(공백) | 코더 플러그인(`plugins/moai`) | 현재 프로젝트의 `product.md`/`structure.md`/`tech.md`/`codemaps/` 생성. `Skill("moai:moai") with arguments: project $ARGUMENTS`를 디스패치한다. | `plugins/moai/commands/project.md` |
| `/moai --project` | 플래그(이중 대시) | `moai-pm` `moai` 스킬(본 스킬) | 개발-프로젝트 초기화 어드바이저: 인터뷰 + 스택 감지 + CLAUDE.md/agents/skills/settings.json/hooks/.mcp.json 생성. | 본 스킬 |

**규칙**: `/moai --project`(플래그)는 `/moai project`(서브커맨드)를 가리거나 대체하거나 가로채지 않는다. 두 진입점은 명확히 분리되어 있다.

### 레거시 `/project` 서브커맨드 목적지 (요약)

레거시 통합 `/project` 스킬의 7개 서브커맨드(`resume`/`catalog`/`status`/`apikey`/`doctor`/`feedback`/`evolve`)는 각각 goose·moai 어드바이저 또는 폐기로 이관되었다. 전체 매핑 표(1개 토큰당 목적지 + 근거)는 `design.md §F.1`을 정본으로 삼는다. `doctor`(환경/툴체인 진단)는 moai 스킬로 이관되었다 — Claude Code 런타임 개발 관심사이기 때문이다(goose는 hooks/LSP 툴체인이 없어 진단 대상이 아니다).

---

## Claude Code Runtime Assumption

moai 스킬이 생성하는 산출물(hooks·LSP 설정·output-styles)은 **Claude Code 런타임**에서 동작한다고 가정한다 — goose(Desktop) 제약의 역이다. Claude Code runtime에서는 hooks·LSP·output-styles가 정상적으로 기능하므로, 이 스킬은 이들을 생성 대상으로 다룬다.

---

## 상세 레퍼런스 (`references/`)

| 파일 | 역할 |
|------|------|
| `router.md` | 자연어 → moai 스킬 라우팅(개발 키워드 매핑) |
| `coder-setup.md` | 5-Phase 정본(유형 인터뷰 → 설치 확인 → 정본 스캐폴드 → 언어·MCP → SPEC 안내) |
| `init-protocol.md` | 인터뷰 스키마·설치 확인·재개(Re-entry) 상세(dev-init 섹션) |
| `execution-protocol.md` | 초기화 실행 핸드오프·품질 게이트 소비 |
| `claudemd-generator.md` | 두-템플릿 분리(HARD) · CLAUDE.md 생성 위임 원칙 |
| `mcp-fallback-summary.md` | 코더 플러그인 부재 시 임베디드 카탈로그 폴백 요약(REQ-M-006) |
| `INDEX.md` | moai 레퍼런스 전체 인덱스 |

---

## 주의사항

1. **글로벌 프로필 질문 금지** — 이름·회사·역할을 재질문하지 않는다.
2. **moai는 직접 구현하지 않는다** — 초기화 산출물 생성 + 라우팅만 담당한다. 실제 SPEC plan/run/sync 워크플로우는 코더 플러그인(`plugins/moai`)이 전담한다.
3. **단일 마켓플레이스 정합** — 모든 스킬 참조는 `moai:` 접두어를 사용한다.
