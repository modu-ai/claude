# moai (코더) — SPEC 기반 개발을 Claude Code만으로 하는 동료

> **코더**는 `moai` CLI **설치 없이** Claude Code 터미널·데스크탑에서 MoAI-ADK의 SPEC 개발 방법론(PLAN › RUN › SYNC)을 쓰는 동료입니다. 개발 환경 셋업부터 DDD/TDD 구현·품질 게이트·문서 동기화까지 `/moai` 명령으로 처리합니다. 비개발자와 개발자 모두 `/moai`로 개발합니다.

---

## 무엇을 하나요 (29스킬)

| 역할 | 언제 | 무엇을 하나요 |
|------|------|---------------|
| 📋 **SPEC 워크플로우** | 새 기능·리팩터링을 시작할 때 | `/moai:plan → run → sync` PLAN›RUN›SYNC 사이클 + SPEC 템플릿 |
| 🧪 **DDD/TDD 구현** | 도메인 모델·테스트 주도 개발 | ANALYZE-PRESERVE-IMPROVE / RED-GREEN-REFACTOR 사이클 |
| ✅ **품질 게이트** | 커밋 전 품질 보증 | TRUST 5 + lint·type-check·test 병렬 게이트 |
| 🔧 **개발 환경 셋업** | 프로젝트 초기화 | `.claude/` + `.moai/` + `CLAUDE.md` 스캐폴드 (MoAI-ADK 정본 패리티) |

> 브랜드·디자인은 **디자이너**가, 실무·글쓰기는 **코워커**가 담당합니다.

---

## 사용법

### SPEC 워크플로우 (PLAN › RUN › SYNC)

```
"인증 기능 SPEC으로 개발해줘"
→ /moai:plan (SPEC 작성) → /moai:run (DDD/TDD 구현) → /moai:sync (문서 동기화 + PR)
```

### `/moai` 명령 (14개)

| 카테고리 | 명령 |
|---------|------|
| 워크플로우 | `/moai:plan` `/moai:run` `/moai:sync` |
| 유틸리티 | `/moai:fix` `/moai:loop` `/moai:clean` `/moai:mx` `/moai:review` |
| 품질 | `/moai:codemaps` `/moai:gate` |
| 프로젝트 | `/moai:project` `/moai:harness` `/moai:feedback` |

- 명령은 flat `commands/*.md` 구조로 번들됩니다(서브디렉토리는 typed 이름에 반영되지 않음).
- 디자인 작업은 `moai-designer` 플러그인의 `/design`을 사용하세요.

---

## 프로젝트 시작하기

처음 개발 환경을 셋업할 때는 **PM** 플러그인의 `/project --code`가 안내합니다.

```
/project --code
"Next.js 프로젝트 SPEC으로 개발하고 싶어"
→ PM이 코더 개발 환경 셋업으로 연결 (.claude/.moai/CLAUDE.md 스캐폴드)
```

자세한 건 [moai-pm README](../moai-pm/README.md)를 참고하세요.

---

## 설치

모두의클로드는 `modu-ai/claude` 마켓플레이스 하나에서 4명의 AI 직원을 설치합니다.

**① 마켓 등록 (최초 1회)**

    /plugin marketplace add modu-ai/claude

**② 이 직원 추가**

    /plugin install moai@moai-claude

또는 `/plugin` 입력 → **"Browse Plugins"** → moai 선택.

> 개발 프로젝트를 시작할 때 설치하세요.
> **재설치 안내 (개명 마이그레이션)** — 본 플러그인은 개명되었습니다. 개명 전 이름으로 설치한 분은 자동 마이그레이션이 제공되지 않으므로, 기존 플러그인을 제거한 뒤 `moai@moai-claude`로 **재설치**해 주세요.

---

## 다른 AI 직원과 함께 쓰기

코더는 4명의 AI 직원 중 한 명입니다.

| AI 직원 | 언제 |
|---------|------|
| 🧑‍💼 코워커 | 실무·콘텐츠·작가 |
| 🎨 디자이너 | 브랜드·디자인 시스템·Claude Design |
| 💻 **코더**(본 플러그인) | 개발·SPEC·품질 게이트 |
| 📋 PM | 프로젝트 시작 허브 (`/project`) |

---

## 더 알아보기 (개발자 기술)

### Desktop Edition 능력 Tier

| Tier | 구성 | 능력 |
|------|------|------|
| **Tier 1** (플러그인 단독) | moai만 설치 | `/moai:plan → run → sync` + SPEC 템플릿 + 14 명령 ≈ 방법론 90% |
| **Tier 2** (플러그인 + git) | Tier 1 + git CLI | 브랜치·워크트리 흐름 (git CLI 직접 호출) |
| **Tier 3** (+ moai 바이너리) | Tier 2 + `moai` CLI 바이너리 | 네이티브 훅 강제(품질 게이트·Stop 훅) + LSP 진단 게이트 + 세션 레지스트리 + cg/glm 비용 모드 |

세션 시작 훅이 `moai` 바이너리를 탐지해 Tier 3 승격을 1줄로 안내하고, 없으면 무음 fail-open합니다 (REQ-BD-009/010, AC-BD-005a/b).

### 코드 인텔리전스 (LSP 5종)

플러그인 루트의 `.lsp.json`이 공식 LSP 서버 5종을 선언합니다. 파일 확장자로 언어를 감지해 해당 서버를 자동 기동하며, 바이너리가 없는 환경(Claude Desktop 등)에서는 graceful skip으로 조용히 넘어갑니다 (`claude --debug`로 확인 가능).

| 언어 | 서버 | 설치 |
|------|------|------|
| Go | gopls | `go install golang.org/x/tools/gopls@latest` |
| Python | pyright | `npm i -g pyright` |
| Rust | rust-analyzer | `brew install rust-analyzer` (또는 rustup) |
| Swift | sourcekit-lsp | Xcode/Swift toolchain 내장 |
| TypeScript | typescript-language-server | `npm i -g typescript-language-server typescript` + 워크스페이스에 `typescript@5` (TS 7 네이티브 프리뷰는 tsserver 미포함) |

편집 직후 diagnostics가 대화 컨텍스트로 주입되어 타입 오류를 즉시 인지합니다. 서버 바이너리는 `$PATH`에서 해석되므로, nvm 등 셸 초기화 의존 경로는 표준 경로(`/opt/homebrew/bin` 등)에 심볼릭 링크를 권장합니다.

### 정본 패리티 (parity-source)

`moai-adk-go` 배포 템플릿 `internal/template/templates/`를 정본으로 무설치 완전 패리티로 재패키징합니다. 각 산출물 상단의 `<!-- parity-source: ... @ <commit> -->` 주석이 정본 커밋을 고정합니다.

> **harness 정본 (D4)** — coder는 무설치 완전 패리티를 위해 `commands/`·`skills/`·`agents/` 외에도 `hooks/`·`output-styles/`·`rules/`·`mcp` 카테고리를 함께 번들합니다. 다른 직원 플러그인(코워커·디자이너·PM)이 skills 중심인 것과 대비되며, coder만이 Claude Code harness 전체를 무설치로 재현합니다.

무설치 적응 — 워크트리 셸아웃→git 직접(`moai worktree new/done`→`git worktree add/remove`), 바이너리 게이트 기능 `[무설치-이연]` 마커 표기, SKILL.md 4-필드 정제(29스킬 `3.1.0` SSOT), 에이전트 `hooks:` 필드 제거, MCP `context7` 정적 선언.

### 패리티 계약 (`/moai:project` ↔ `moai init`)

`/moai:project`(무설치)와 `moai init`(바이너리)은 동일 `.claude/` + `.moai/` 파일 트리를 생성합니다 (REQ-BD-005, AC-BD-002). 유일한 값 발산은 `.moai/config/sections/system.yaml`의 `version` 필드 — 바이너리는 실제 버전, 무설치는 `plugin-deployed vX.Y.Z` 리터럴 마커 (REQ-BD-006).

### 버전 SSOT (Release Bump Checklist)

⚠️ 릴리스 버전 4개 위치 일괄 bump (REQ-BD-011):

1. `pkg/version/version.go` — 바이너리 정본 (`Version = "vX.Y.Z"`)
2. `internal/template/templates/.moai/config/sections/system.yaml.tmpl` — `{{.Version}}` 플레이스홀더
3. `plugins/moai-coworker/.claude-plugin/plugin.json`
4. `plugins/moai/.claude-plugin/plugin.json`

플러그인 버전은 바이너리 `3.0.x` 라인에 바인딩 (REQ-BD-012). `www/hugo.toml` L50-54의 ⚠️SSOT 주석이 원천.

### 빌드

```bash
bash scripts/render-templates.sh   # 정본 → 플러그인 트리 렌더/복사
```

---

**라이선스**: LicenseRef-MoAI-NC-ND-1.0 · **작성자**: 모두의AI · **버전**: 3.1.0
