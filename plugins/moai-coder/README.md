# moai-code — MoAI-ADK 무설치 플러그인

`moai` CLI **설치 없이** Claude Code 터미널·데스크탑에서 MoAI-ADK의 SPEC 개발 방법론(PLAN › RUN › SYNC)을 사용하는 플러그인입니다. **비개발자와 개발자 모두** `/moai` 명령으로 개발합니다.

## Desktop Edition 능력 Tier

`moai-code`는 **moai-adk Desktop Edition**으로, 올인원 설치 상태를 유지하면서 **"필요한 것만"은 프로젝트 시점에 스킬 프로파일(`.moai/skill-profile.yaml`)로 조준**되는 구조다. 설치 시점이 아니라 프로젝트 시점의 선택적 활성화가 핵심이다.

| Tier | 구성 요소 | 능력 |
|------|----------|------|
| **Tier 1** (플러그인 단독) | moai-code 플러그인만 설치 | `/moai:plan → run → sync` 워크플로우 + SPEC 템플릿 + 13개 명령 ≈ 방법론 90% |
| **Tier 2** (플러그인 + git) | Tier 1 + git CLI | 브랜치·워크트리 흐름(git CLI 직접 호출) |
| **Tier 3** (플러그인 + moai 바이너리) | Tier 2 + `moai` CLI 바이너리 | 네이티브 훅 강제(품질 게이트·Stop 훅) + LSP 진단 게이트 + 세션 레지스트리 + cg/glm 비용 모드 |

세션 시작 훅(`hooks/moai/handle-session-start.sh`)이 `moai` 바이너리를 탐지해 Tier 3 승격 안내를 1줄로 표시하고, 바이너리가 없으면 무음 fail-open한다(REQ-BD-009 / REQ-BD-010, AC-BD-005a/b).

## 설치

```bash
claude plugin marketplace add modu-ai/claude
/plugin install moai-code
```

## 명령 (14개)

플러그인 명령은 `플러그인명:명령` 콜론 네임스페이스로 노출됩니다. 이 플러그인의 `name`은 `moai`이므로 명령은 **`/moai:<name>`** 형태입니다(예: `/moai:plan`).

| 카테고리 | 명령 |
|---------|------|
| 워크플로우 | `/moai:plan` `/moai:run` `/moai:sync` |
| 유틸리티 | `/moai:fix` `/moai:loop` `/moai:clean` `/moai:mx` `/moai:review` |
| 품질 | `/moai:codemaps` `/moai:gate` `/moai:security` |
| 프로젝트 | `/moai:project` `/moai:harness` `/moai:feedback` |

- 명령은 flat `commands/*.md` 구조로 번들됩니다(서브디렉토리는 플러그인에서 typed 이름에 반영되지 않음 — 공식 문서 검증).
- 디자인 작업은 `moai-design` 플러그인의 `/design`을 사용하세요(D7 위임).
- `coverage`·`e2e`는 정본에서 은퇴되었습니다.

## 정본 기준 (parity-source)

이 플러그인은 `moai-adk-go`의 배포 템플릿 `internal/template/templates/`를 정본으로 삼아 무설치 완전 패리티로 재패키징합니다. 각 렌더 산출물 상단의 `<!-- parity-source: ... @ <commit> -->` 주석이 정본 커밋을 고정합니다.

### 무설치 적응 (SPEC-MOC-PLUGIN-CODE-001 P1)

정본을 그대로 복사하되, `moai` 바이너리에 의존하는 지점을 무설치 등가물로 치환합니다:

- **워크트리 셸아웃 → git 직접**: 라우터 워크플로우의 `moai worktree new/done`을 `git worktree add`/`git worktree remove` + 브랜치 setup으로 치환(분기 옵션 `--base`/`--from-current`/`--tmux`/`--delete-branch` 의미 보존).
- **바이너리 게이트 기능 이연 표기**: `moai hook db-schema-sync`·`moai harness <verb>`처럼 바이너리 없이는 비기능인 참조는 `[무설치-이연]` 마커로 문서화(동작을 바꾸는 placeholder로 조용히 대체하지 않음).
- **SKILL.md frontmatter 정제**: 28개 스킬을 4-필드(`name`/`description`/`user-invocable`/`version`)로 정제, 버전 SSOT `3.0.0` 단일화.
- **에이전트 `hooks:` 필드 제거**: `handle-agent-hook.sh` 셸아웃에 의존하는 4개 에이전트 프론트매터 `hooks:` 블록 제거.
- **MCP 서버**: `.mcp.json`에 `context7`(최신 라이브러리 문서 조회) 1개를 정적 선언(플랫폼 조건은 non-Windows 기본 분기로 해소, Windows 대체는 주석 문서화).

## 패리티 계약 (`/moai:project` ↔ `moai init`)

`/moai:project`(무설치)와 `moai init`(바이너리)은 **동일 `.claude/` + `.moai/` 파일 트리**를 생성한다(REQ-BD-005 / AC-BD-002).

**유일한 값 발산 지점**: `.moai/config/sections/system.yaml`의 `version` 필드.
- `moai init`(바이너리): 템플릿 정본의 `{{.Version}}` 플레이스홀더가 실제 바이너리 버전으로 렌더링된다(예: `3.0.0-rc6`).
- `/moai:project`(무설치): 바이너리 셸아웃이 없으므로 템플릿 렌더링이 불가하다 → 리터럴 마커 `"plugin-deployed vX.Y.Z"`를 `system.yaml`의 `version` 필드에 기입한다(REQ-BD-006 / AC-BD-003). 이 `plugin-deployed` 마커는 나중에 `moai doctor`가 탐지해 바이너리 관리 트리로의 승격을 제안하는 착지점이 된다(REQ-BD-007 — 본 SPEC 범위 외, 후속 SPEC).

**검증 하네스 (AC-BD-002 RUNTIME)** — 두 진입점의 산출 트리를 빈 디렉터리 A, B에서 각각 실행 후 비교:

```bash
CNT_A=$(cd A && find .claude .moai -type f | wc -l)
CNT_B=$(cd B && find .claude .moai -type f | wc -l)
[ "$CNT_A" -gt 10 ] && [ "$CNT_B" -gt 10 ] || { echo "FAIL: 빈 트리(하네스 미실행)"; exit 1; }
diff <(cd A && find .claude .moai -type f | sort) \
     <(cd B && find .claude .moai -type f | sort)   # 출력 없음 = PASS(버전 라인만 유일한 발산)
# 값 발산 1지점 확인:
grep '^\s*version:' B/.moai/config/sections/system.yaml   # → "plugin-deployed vX.Y.Z"
grep '^\s*version:' A/.moai/config/sections/system.yaml   # → 실제 바이너리 버전
```

`non-empty` 가드(`> 10`)는 빈-vs-빈 거짓 통과를 차단한다. 파일 집합 자체는 동일하며, 유일한 값 발산은 위 한 줄뿐이다.

## 버전 스탬프 SSOT (Release Bump Checklist)

⚠️ VERSION-SSOT — 릴리스 버전 4개 위치 일괄 bump 체크리스트 (REQ-BD-011):

1. `pkg/version/version.go` — 바이너리 정본 (`Version = "vX.Y.Z"`)
2. `internal/template/templates/.moai/config/sections/system.yaml.tmpl` — `{{.Version}}` 플레이스홀더 (정본 주입, 리터럴 아님 — AC-BD-006b PRESERVE)
3. `plugins/moai-coworker/.claude-plugin/plugin.json` — `"version": "X.Y.Z"`
4. `plugins/moai-code/.claude-plugin/plugin.json` — `"version": "X.Y.Z"`

**릴리스 체크리스트**: 위 4개 위치를 동일 버전으로 일괄 bump 후 배포한다. 플러그인 버전은 바이너리 v3.0.x 라인에 바인딩(REQ-BD-012, `3.0.x ↔ 3.0.x`).

**정규화 비교 (AC-BD-006d D1-GATED)** — `v` 접두·`-rcN` pre-release 접미사 제거 후 concrete 리터럴 3곳 일치:
- `pkg/version/version.go`: `v3.0.0-rc6` → 정규화 `3.0.0`
- `plugins/moai-coworker/.claude-plugin/plugin.json`: `3.0.0` → `3.0.0`
- `plugins/moai-code/.claude-plugin/plugin.json`: `3.0.0` → `3.0.0`

참고: `www/hugo.toml` L50-54의 ⚠️SSOT 주석 블록이 이 패턴의 원천이며, 마켓플레이스 메타데이터(`.claude-plugin/marketplace.json`)는 본 4-location 열거 밖이므로 별도 릴리스 단계에서 다룬다.

## 빌드

```bash
bash scripts/render-templates.sh   # 정본 → 플러그인 트리 렌더/복사 (P1)
```

## 설계 문서

- 아키텍처: `docs/plugin-family-design/02-moai-code.md`
- 구축 스펙: `docs/plugin-family-design/04-moai-code-processing.md`

## 라이선스

LicenseRef-MoAI-NC-ND-1.0
