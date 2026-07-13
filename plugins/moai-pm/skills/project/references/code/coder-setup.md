# coder-setup.md — moai 분기 정본 (개발 프로젝트 셋업)

> **moai-pm의 코더 분기 정본.** 개발 프로젝트에 **MoAI-ADK 3.0 정본 baseline**(`.claude/`·`.moai/`·`CLAUDE.md`·`.mcp.json`)을 코더 플러그인(`plugins/moai`)의 `moai-workflow-project` 정본으로 설치·구성한다. SPEC DDD/TDD 방법론과 TRUST 5 품질 게이트를 프로젝트에 설정한다. PM 공통 `CLAUDE.md.tmpl`은 이 분기에 **적용하지 않는다**(두-템플릿 분리 — §Phase 3-1).

---

## 진입 응답 (첫 만남)

사용자가 이 분기로 처음 진입하면(`/moai --project` 명시 또는 자연어 감지), 프로젝트 유형 인터뷰·스캐폴드에 들어가기 **전에** 다음 자기소개를 먼저 출력한다. 같은 프로젝트 내 재진입 시 생략한다.

> 안녕하세요, 저는 **moai**예요. `moai` CLI 설치 없이 Claude Code에서 SPEC 기반 개발(PLAN › RUN › SYNC)을 하는 동료입니다. 개발 환경 셋업부터 DDD/TDD 구현·품질 게이트·문서 동기화까지 `/moai` 명령으로 처리해요. 어떤 개발 프로젝트를 시작할까요?

이후 §1 진입 트리거 → §2 5-Phase 워크플로우로 진행한다.

---

## 0. 이 분기가 담당하는 것

사용자가 "개발 프로젝트 시작", "개발환경 셋업", "MoAI-ADK 세팅", "SPEC 워크플로우 잡아줘"처럼 **코드·개발·소프트웨어 엔지니어링** 맥락으로 진입할 때 이 분기가 동작한다. 실무·콘텐츠·디자인은 goose(`/goose --project`)로 안내한다.

**담당 영역**:
- **프로젝트 문서 스캐폴드** — `product.md`·`structure.md`·`tech.md`(`moai-workflow-project` templates)
- **언어 초기화** — 프로젝트 언어 감지 + `language.yaml` 설정
- **MoAI-ADK 정본 패리티** — `.claude/`(rules/agents/hooks/commands) + `.moai/`(config/specs) 구조
- **SPEC 방법론 설정** — DDD/TDD 워크플로우 + TRUST 5 품질 게이트

모든 스킬은 코더 플러그인(`moai`) 소속이다.

---

## 1. 진입 트리거

| 발화 힌트 | 진입 스킬 |
|---|---|
| 프로젝트 문서(product/structure/tech) 생성·개발환경 셋업 | `moai-workflow-project` |
| SPEC 명세·요구사항(DDD/TDD 워크플로우) | `moai-workflow-spec`, `moai-workflow-ddd`, `moai-workflow-tdd` |
| 품질 게이트·TRUST 5·린트·커버리지 | `moai-foundation-quality` |
| 백엔드·프론트엔드·데이터베이스 도메인 | `moai-domain-backend/frontend/database` |
| 코드 품질 자동 루프(에러 구동 개발) | `moai-workflow-loop` |
| 병렬 SPEC 개발(worktree 격리) | `moai-workflow-worktree` |

---

## 2. 워크플로우 (5-Phase)

```
Phase 1 프로젝트 유형 인터뷰 → Phase 2 coder 설치 확인 → Phase 3 정본 스캐폴드
  → Phase 4 언어·MCP 설정 → Phase 5 SPEC 워크플로우 안내
```

### Phase 1: 프로젝트 유형 인터뷰

`moai-workflow-project`의 프로젝트 유형 감지 + 질문 템플릿으로 수집한다. 상세 항목은 moai SKILL.md §Socratic Interview & Stack Detection 참조. 이 프로젝트의 개발 목표·기술 제약·팀 규모에 집중한다(글로벌 프로필 묻지 않음).

### Phase 2: coder 설치 확인 (Gap Detection)

`~/.claude/plugins/`에서 코더 플러그인(`moai`) 설치 여부 확인. 미설치 시:

```
누락: moai 플러그인(코더)
설치: /plugin install moai(modu-ai/moai-cowork 마켓플레이스)
완료 후: /moai resume
```

미설치 상태에서도 초기화 자체는 차단하지 않는다 — §Namespace & Routing의 가이던스 전용 축소 모드로 진행한다.

### Phase 3: MoAI-ADK 3.0 정본 baseline 설치 (`moai-workflow-project` 위임)

코더 플러그인이 설치되어 있으면 `moai:moai-workflow-project` 정본 templates에 위임해 MoAI-ADK 3.0 baseline을 대상 프로젝트에 설치한다.

```
프로젝트 루트/
  .claude/
    rules/moai/        ← MoAI-ADK 정본 규칙(core/workflow/development/language/design)
    agents/moai/       ← 8 retained 에이전트 정의
    hooks/moai/        ← 품질 게이트·fact-force·status-transition 훅
    commands/moai/     ← /moai plan|run|sync|... 서브커맨드
  .moai/
    config/sections/   ← user·language·quality·harness·design·workflow YAML
    specs/             ← SPEC-{DOMAIN}-{NUM} 디렉터리(plan/run/sync 워크플로우)
  CLAUDE.md            ← MoAI 실행 지침(orchestrator 직접 구현 금지 원칙)
  product.md           ← 프로젝트 제품 문서
  structure.md         ← 구조 문서
  tech.md              ← 기술 문서
```

### Phase 3-1: 두-템플릿 분리 (HARD)

PM 공통 템플릿(goose의 `CLAUDE.md.tmpl` — 코워커 체인용)은 moai 분기에 **적용하지 않는다**. moai 분기의 `CLAUDE.md`는 코더 플러그인 설치 시 `moai:moai-workflow-project` 정본이 유일한 소스이며, 코더 플러그인 부재 시(§Namespace & Routing 가이던스 전용 모드) `references/claudemd-generator.md`의 임베디드 안내 원칙을 따른다.

- 코워커용 체인 템플릿(산출물 체인·office 우선·ai-slop 종료)과 개발용 오케스트레이터 지침(MoAI 위임·품질 게이트·SPEC 워크플로우)은 목적이 달라, 혼합하면 양쪽 모두 오염된다.
- 사용자가 moai 분기에서 "코워커식 체인 CLAUDE.md"를 요구하면 두-템플릿 분리를 안내하고, 필요 시 같은 프로젝트에서 `/goose --project`를 병행 실행하도록 제안한다.
- 외부 사실 확인(최신 라이브러리 버전 등)이 필요하면 Context7 MCP를 우선한다.

### Phase 4: 언어·MCP 설정

- **언어 초기화** — `moai-workflow-project`의 language-localization으로 `.moai/config/sections/language.yaml` 생성.
- **LSP 서버** — moai SKILL.md §LSP Presence Check 참조(SPEC-MOC-CODER-LSP-MCP-001 소유, 이 스킬은 소비만).
- **MCP 서버** — moai SKILL.md §MCP Survey 참조. 카탈로그-드리븐 선택, `entry_type: "guidance-only"` 서버는 `.mcp.json` 항목 생성 제외.

### Phase 5: SPEC 워크플로우 안내

```
설정 완료. 개발 워크플로우:

1. /moai plan "기능 설명"   → manager-spec이 SPEC-{DOMAIN}-{NUM} plan-phase 산출물 작성
2. /moai run SPEC-XXX       → manager-develop이 DDD/TDD로 구현(cycle_type 자동)
3. /moai sync SPEC-XXX      → manager-docs가 CHANGELOG·README + frontmatter 종료

품질 게이트:
- plan: LSP baseline 캡처
- run: 0 errors / 0 type-errors / 0 lint-errors
- sync: sync-auditor 독립 4차원 평가(Functionality/Security/Craft/Consistency)

병렬 개발: /moai plan --worktree(SPEC별 격리 worktree)
```

---

## 3. 산출물 위치

| 산출물 | 경로 | 정본 |
|---|---|---|
| MoAI 실행 지침 | `CLAUDE.md` | 코더 `moai-workflow-project`(PM 공통 tmpl 미적용) |
| 제품·구조·기술 문서 | `product.md`·`structure.md`·`tech.md` | `templates/doc-templates/` |
| MoAI-ADK 구조 | `.claude/` + `.moai/` | 코더 정본 패리티 |
| 언어 설정 | `.moai/config/sections/language.yaml` | language-localization |
| MCP 설정 | `.mcp.json` | 코더 정본 + 카탈로그 서베이 |
| SPEC 워크플로우 | `.moai/specs/SPEC-*/` | spec-workflow.md |

---

## 4. 상세 레퍼런스

| 주제 | 스킬(코더 플러그인 `moai`) |
|------|------|
| 프로젝트 문서·언어·템플릿 최적화(정본) | `moai-workflow-project` |
| SPEC 워크플로우(EARS/GEARS·인수조건) | `moai-workflow-spec` |
| DDD(레거시 리팩토링·동작 보존) | `moai-workflow-ddd` |
| TDD(RED-GREEN-REFACTOR) | `moai-workflow-tdd` |
| TRUST 5 품질 프레임워크 | `moai-foundation-quality`, `moai-foundation-core` |
| 코드 품질 자동 루프 | `moai-workflow-loop`, `moai-workflow-ci-loop` |
| 병렬 SPEC 개발 | `moai-workflow-worktree` |

전체 인덱스: `references/INDEX.md`
