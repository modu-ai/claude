# coder-setup.md — `/project --code` 분기 (코더 개발 환경 셋업)

> **4-plugin 허브 라우터의 코더 분기 정본.** 개발 프로젝트의 `.claude/`·`.moai/`·`CLAUDE.md`·`.mcp.json` 정본 스캐폴드를 `moai-coder` 플러그인의 `moai-workflow-project` 정본(templates 11종)으로 생성한다. SPEC DDD/TDD 방법론과 TRUST 5 품질 게이트를 프로젝트에 설정한다.

---

## 0. 이 분기가 담당하는 것

사용자가 "개발 프로젝트 시작", "개발환경 셋업", "MoAI-ADK 세팅", "SPEC 워크플로우 잡아줘"처럼 **코드·개발·소프트웨어 엔지니어링** 맥락으로 진입할 때(`--code` 플래그 명시 또는 자연어 감지) 이 분기가 동작한다. 실무·콘텐츠는 `--cowork`, 디자인은 `--designer` 분기로 라우팅된다(SKILL.md 허브 참조).

**담당 영역**:
- **프로젝트 문서 스캐폴드** — `product.md`·`structure.md`·`tech.md` (moai-workflow-project templates)
- **언어 초기화** — 프로젝트 언어 감지 + `language.yaml` 설정
- **MoAI-ADK 정본 패리티** — `.claude/`(rules/agents/hooks/commands) + `.moai/`(config/specs) 구조
- **SPEC 방법론 설정** — DDD/TDD 워크플로우 + TRUST 5 품질 게이트

모든 스킬은 **`moai-coder` 단일 플러그인** 소속이다.

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

`moai-workflow-project`의 프로젝트 유형 감지 + 질문 템플릿(`templates/question-templates/`)으로 수집:

| 질문 영역 | 수집 내용 |
|---|---|
| 프로젝트 유형 | 웹 앱·모바일·CLI·라이브러리·ML 프로젝트 |
| 기술 스택 | 언어·프레임워크·DB·주요 의존성 |
| 문서 언어 | ko·en·ja·zh (기본 ko, 비개발자 친화) |
| 품질 게이트 깊이 | minimal·standard·thorough (harness level) |
| 개발 방법론 | DDD(레거시 리팩토링) / TDD(신규 기능) 자동 선택 기준 |

인터뷰는 **이 프로젝트의 개발 목표·기술 제약·팀 규모**에 집중한다(글로벌 프로필 묻지 않음 — cowork 분기와 동일 원칙).

### Phase 2: coder 설치 확인 (Gap Detection)

`~/.claude/plugins/` 에서 `moai-coder` 설치 여부 확인(Bash + system reminder 교차 검증). 미설치 시:

```
누락: moai-coder 플러그인
설치: /plugin install moai-coder (modu-ai/claude 마켓플레이스)
완료 후: /project resume --code
```

### Phase 3: 정본 스캐폴드 (`moai-workflow-project` 위임)

`moai-coder:moai-workflow-project` 정본 templates로 산출물 생성:

```
프로젝트 루트/
  .claude/
    rules/moai/        ← MoAI-ADK 정본 규칙(core/workflow/development/language/design)
    agents/moai/       ← 8 retained 에이전트 정의
    hooks/moai/        ← 품질 게이트·fact-force·status-transition 훅
    commands/moai/     ← /moai plan|run|sync|... 서브커맨드
  .moai/
    config/sections/   ← user·language·quality·harness·design·workflow YAML
    specs/             ← SPEC-{DOMAIN}-{NUM} 디렉토리 (plan/run/sync 워크플로우)
  CLAUDE.md            ← MoAI 실행 지침 (orchestrator 직접 구현 금지 원칙)
  product.md           ← 프로젝트 제품 문서 (templates/doc-templates/product-template.md)
  structure.md         ← 구조 문서 (structure-template.md)
  tech.md              ← 기술 문서 (tech-template.md)
```

`moai-workflow-project`의 config-template.json·doc-templates·question-templates가 변수 치환을 담당한다.

### Phase 4: 언어·MCP 설정

- **언어 초기화** — `moai-workflow-project`의 language-localization으로 `.moai/config/sections/language.yaml` 생성(대화 언어·코드 주석·커밋 메시지·문서 언어)
- **MCP 서버** — `.mcp.json`에 Context7(최신 라이브러리 문서)·claude-in-chrome 등 필수 MCP 배선. 프로젝트가 요구하면 추가(Higgsfield·ElevenLabs 등은 cowork/designer 분기와 공유)

### Phase 5: SPEC 워크플로우 안내

```
설정 완료. 개발 워크플로우:

1. /moai plan "기능 설명"   → manager-spec이 SPEC-{DOMAIN}-{NUM} plan-phase 산출물 작성
2. /moai run SPEC-XXX       → manager-develop이 DDD/TDD로 구현 (cycle_type 자동)
3. /moai sync SPEC-XXX      → manager-docs가 CHANGELOG·README + frontmatter 종료

품질 게이트:
- plan: LSP baseline 캡처
- run: 0 errors / 0 type-errors / 0 lint-errors (golangci-lint·eslint·ruff·clippy 자동 감지)
- sync: sync-auditor 독립 4차원 평가 (Functionality/Security/Craft/Consistency)

병렬 개발: /moai plan --worktree  (SPEC별 격리 worktree)
```

---

## 3. 산출물 위치

| 산출물 | 경로 | 정본 |
|---|---|---|
| MoAI 실행 지침 | `CLAUDE.md` | coder `moai-workflow-project` |
| 제품·구조·기술 문서 | `product.md`·`structure.md`·`tech.md` | `templates/doc-templates/` |
| MoAI-ADK 구조 | `.claude/` + `.moai/` | coder 정본 패리티 |
| 언어 설정 | `.moai/config/sections/language.yaml` | language-localization |
| MCP 설정 | `.mcp.json` | coder 정본 |
| SPEC 워크플로우 | `.moai/specs/SPEC-*/` | spec-workflow.md |

---

## 4. 상세 레퍼런스

| 주제 | 스킬 (moai-coder) |
|------|------|
| 프로젝트 문서·언어·템플릿 최적화(정본) | `moai-workflow-project` |
| SPEC 워크플로우(EARS/GEARS·인수조건) | `moai-workflow-spec` |
| DDD(레거시 리팩토링·동작 보존) | `moai-workflow-ddd` |
| TDD(RED-GREEN-REFACTOR) | `moai-workflow-tdd` |
| TRUST 5 품질 프레임워크 | `moai-foundation-quality`, `moai-foundation-core` |
| Claude Code 오소링(스킬·에이전트·훅) | `moai-foundation-cc` |
| 코드 품질 자동 루프 | `moai-workflow-loop`, `moai-workflow-ci-loop` |
| 병렬 SPEC 개발 | `moai-workflow-worktree` |
| 테스트 피라미드·품질 평가 | `moai-workflow-testing`, `moai-ref-testing-pyramid` |

전체 인덱스: `references/core/INDEX.md`
