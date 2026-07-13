# init-protocol.md — `/moai --project` 초기화 전체 플로우 (dev-init)

## 개요

`/moai --project`는 개발 프로젝트를 초기화하고, 프로젝트 유형·기술 스택을 인터뷰/감지한 뒤, MoAI-ADK 3.0 정본 baseline을 설치·구성한다. 글로벌 프로필 시스템은 사용하지 않는다.

---

## 전체 플로우

```
/moai --project
    ↓
Phase 1: 프로젝트 유형 인터뷰 + 스택 자동 감지
    ↓
Phase 2: coder 플러그인 설치 확인(Gap Detection)
    ↓
Phase 3: MoAI-ADK 3.0 정본 baseline 설치(또는 가이던스 전용 축소 모드)
    ↓
Phase 4: 언어·LSP·MCP 설정
    ↓
Phase 5: SPEC 워크플로우 안내
```

상세 Phase별 내용은 `coder-setup.md` §2를 정본으로 삼는다(단일 소스 — 중복 유지 안 함).

---

## Phase 1: 프로젝트 유형 인터뷰 (상세)

### 1-1. 프로젝트 유형

`AskUserQuestion`(1질문, 4옵션):

```
"어떤 유형의 프로젝트인가요?"
○ 웹 애플리케이션
○ CLI 도구 / 라이브러리
○ 모바일 애플리케이션
○ ML/데이터 프로젝트
+ Other
```

### 1-2. 스택 자동 감지 확인

프로젝트 루트 매니페스트(`package.json`/`go.mod`/`pyproject.toml`/`Cargo.toml`)를 스캔해 후보를 도출하고, 감지 결과를 `AskUserQuestion`으로 확인만 받는다(재입력 요구 금지). 매니페스트가 없으면(신규 프로젝트) 자유입력으로 수집한다.

### 1-3. 문서 언어 + 품질 게이트 깊이

`AskUserQuestion`(1질문, 4옵션): 문서 언어(ko/en/ja/zh) — 기본 ko. 품질 게이트 깊이(minimal/standard/thorough)는 harness.yaml 초기값으로 제안하고 필요 시 조정한다.

수집 결과는 메모리에 임시 저장되며, Phase 3에서 `.moai/config/sections/*.yaml`에 직접 기록된다.

---

## Phase 2: coder 설치 확인 (Gap Detection)

`~/.claude/plugins/`에서 코더 플러그인(`moai`) 설치 여부를 확인한다(Bash + system reminder 교차 검증). 미설치 시 설치 명령을 안내하고 `/moai resume`으로 재개하도록 안내하되, 초기화 자체를 차단하지 않는다 — 가이던스 전용 축소 모드(moai SKILL.md §Namespace & Routing)로 계속 진행할 수 있다.

```json
{
  "scanned_at": "2026-07-11T00:00:00+09:00",
  "coder_plugin_installed": false,
  "mode": "guidance-only"
}
```

---

## Phase 3: 정본 baseline 설치 (또는 가이던스 전용)

**코더 플러그인 설치됨**: `moai:moai-workflow-project`에 위임해 `coder-setup.md` §Phase 3 산출물을 생성한다.

**코더 플러그인 미설치**: 가이던스 전용 축소 모드로 전환한다. 생성 산출물: 설치 안내 + `references/mcp-fallback-summary.md`의 임베디드 카탈로그 요약. 실행 라우팅은 시도하지 않는다.

---

## Phase 4: 언어·MCP 설정 (상세)

언어 초기화·LSP 점검·MCP 서베이는 moai SKILL.md §LSP Presence Check / §MCP Survey를 정본으로 삼는다.

---

## Phase 5: SPEC 워크플로우 안내

`coder-setup.md` §Phase 5 안내 메시지를 그대로 사용한다.

---

## Re-entry: 설치 완료 후 진행 재개

| 트리거 | 처리 |
|--------|------|
| `/moai resume` | 명시적 재개 커맨드 |
| "이어서 진행" / "설치 완료" | 자연어 → resume 흐름 자동 트리거 |

복원 흐름: 기존 `.moai/config/sections/*.yaml` + `CLAUDE.md` 로드 → Phase 2 재실행(설치 확인) → 여전히 미설치면 가이던스 전용 모드 유지, 설치 확인되면 Phase 3부터 정상 진행.

---

## `/moai apikey` — API 키 관리

코더 정본이 요구하는 MCP 서버 자격증명을 `.env` 가이던스로 안내한다(실제 값은 절대 기록하지 않음).

---

## `/moai doctor` — 환경 진단

Claude Code 런타임·LSP 설치·hooks 배선 상태를 진단한다(goose의 `/goose doctor`와 달리 Claude Code 개발 툴체인 대상).
