# SPEC-MOC-PLUGIN-MOAI-V2-001 — 진행 상황 (progress)

## §E.1 Plan-phase Audit-Ready Signal

```yaml
plan_status: audit-ready
plan_complete_at: 2026-07-09T05:10:22Z
plan_audit: "iter-1 FAIL 0.88 (6결함) → iter-2 PASS 0.97 (잔존 0) — .moai/reports/plan-audit/SPEC-MOC-PLUGIN-MOAI-V2-001-2026-07-09.md"
artifacts: [spec.md, plan.md, acceptance.md, design.md, research.md, progress.md]
tier: L
open_decisions: []  # DP-1("1.0.0" 리셋)·DP-2(gateguard vendor) 모두 2026-07-09 사용자 확정 — plan.md §H
census_head: 6f92d86
```

## §G IGGDA Kickoff Predicate

- (a) 의도 명확성 100%: PASS — 설계 v2 결정 레지스터 D-1~D-5 + DP-1/DP-2 + Tier/Git 전략 전부 사용자 확정
- (b) plan-auditor PASS: PASS — iter-2 0.97 (임계 0.85)
- (c) Tier S/M: **FAIL — Tier L**
- (d) 위험 키워드/파괴 범위: 해당 없음 (단 (c) 선행 실패)
- 판정: **explicit-gate** (Implementation Kickoff Approval은 차단형 AskUserQuestion으로 진행)
- 평가 시각: 2026-07-09T05:10:22Z
- Implementation Kickoff Approval: **승인** (2026-07-09) — "Mode 5 순차 M1→M6" 차단 AskUserQuestion 응답

## §F Phase 0.95 Mode Selection

```yaml
# Input parameters (collected 2026-07-09, pre-flight 드리프트 0)
tier: L
scope_files: "100+ (M1 git mv 트리 ~354 + M2 rules 61 + config ≥27 + CLAUDE.md + settings + M3 dispatch+gates + M4 scaffold + M5 다수 문서)"
domain_count: 6   # hooks(sh) / templates(md+yaml) / scripts(sh) / manifests(json) / docs(README+www) / config(yaml)
file_language_mix: "markdown + shell + yaml + json (컴파일 없음, 코딩-헤비 아님 — restructuring)"
concurrency_benefit: LOW   # M1 개명이 M2~M6 전부의 전제(plugins/moai/ 경로), 강한 순차 의존
agent_teams_prereqs:
  env_var: "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 (설정됨)"
  harness_level: "thorough 여부 무관 — Mode 5 선택에 영향 없음"
  team_enabled: "무관 — Mode 5 선택"
implementation_kickoff_approval: "승인 — Mode 5 순차 M1→M6 (2026-07-09 explicit-gate 차단 AskUserQuestion)"
```

Mode evaluation (6 modes):

| Mode | Selected? | Rationale |
|---|---|---|
| 1 trivial | No | Tier L + 6 마일스톤, 단순 typo 아님 |
| 2 background | No | Write 작업 다수 (background-write 제한) |
| 3 agent-team | No | restructuring + 순차 의존; team 오버헤드 불필요 |
| 4 parallel | No | M1 개명이 M2-M6 전제 → 병렬화 불가 |
| 5 sub-agent | **Yes (선택)** | 마일스톤별 순차 위임. 코딩-헤비 아닌 restructuring이나 순차 의존이 결정적 |
| 6 workflow | No | 다규칙/의존성 작업 — Mode 6은 단일 기계 변환만 허용; Anthropic 병렬화 경고 |

Decision: sub-agent

Justification: 본 SPEC은 행위 보존 재구조화(rename + move + 참조 갱신)로 코딩-헤비가 아니지만, M1(개명)이 M2~M6 전부의 경로 전제(plugins/moai/)라 강한 순차 의존이 존재. Anthropic 코딩-병렬화 경고("대부분의 코딩 작업은 연구보다 진정 병렬화 가능한 작업이 적다")와 마일스톤 순차 의존성이 일치 → Mode 5(순차 sub-agent)가 안전한 기본값. 마일스톤별 manager-develop 위임 + Hybrid Trunk main-direct push로 단일 에이전트 컨텍스트 한계 회피하면서 각 마일스톤 AC 검증.

## §E.2 Run-phase Evidence

### M1 — 개명 + 마켓 갱신 (AC-MV2-001a·b·c·d)

**Claim**: `plugins/moai-coder/` → `plugins/moai/` 개명 완료(git mv 354 entries rename), manifest·marketplace 갱신(name=`moai`·version=`"1.0.0"` DP-1·source=`./plugins/moai`·톰스톤 0), Layer-1 인벤토리 보존.

**Evidence (verbatim AC outputs, 2026-07-09)**:

AC-MV2-001a (NET-NEW+REMOVAL):
```
$ test -d plugins/moai && test ! -d plugins/moai-coder; echo "exit=$?"
exit=0
```

AC-MV2-001b (NET-NEW):
```
$ jq -r '.name, .displayName, .version' plugins/moai/.claude-plugin/plugin.json
moai
코더
1.0.0
```

AC-MV2-001c (NET-NEW+REMOVAL):
```
$ jq -r '.plugins[].name' .claude-plugin/marketplace.json
moai-coworker
moai-designer
moai
moai-pm
$ jq '.plugins | length' .claude-plugin/marketplace.json
4
$ jq -r '.plugins[] | select(.name=="moai") | .source' .claude-plugin/marketplace.json
./plugins/moai
$ jq '.plugins[] | select(.name=="moai-coder")' .claude-plugin/marketplace.json | wc -l
0
```
→ 4-plugin 유지, `moai` 포함, `moai-coder` 톰스톤 0 (REQ-MV2-003 PASS).

AC-MV2-001d (PRESERVE — self-pass 의도됨):
```
$ find plugins/moai/commands -name '*.md' | wc -l          → 14
$ find plugins/moai/agents -type f | wc -l                 → 8
$ ls -d plugins/moai/skills/*/ | wc -l                     → 29
$ find plugins/moai/output-styles -maxdepth 1 -type f | wc -l → 2 (einstein.md, moai.md)
$ test -f plugins/moai/.mcp.json && echo ".mcp.json present" → .mcp.json present
```
→ commands 14 · agents 8 · skills 29 · output-styles 2 · .mcp.json — 기준선(research.md §E, census_head 6f92d86)과 동일(PRESERVE characterization).

Regression guard (PRESERVE-RUNTIME):
```
$ claude plugin validate ./plugins/moai; echo "exit=$?"
✔ Validation passed with warnings
exit=0
$ claude plugin validate .claude-plugin/marketplace.json; echo "exit=$?"
✔ Validation passed with warnings
exit=0
```

**Baseline-attribution**: 기준선 HEAD cdbc808(병렬 세션 SPEC-MOC-PM-REDESIGN-001 plan-phase — plugins/ 비중첩 확인). rename 전 인벤토리(14/8/29/2/.mcp.json)는 §C.3 pre-flight에서 캡처, rename 후 상기 Evidence와 동일(PRESERVE 회귀 가드 통과). marketplace validate HEAD에서 PASS → rename 후에도 PASS(라벨된 self-pass).

**Gaps**: `P0-8-verdict:` 센티넬 라인 — M6 소관(AC-MV2-006c). M1 범위 외; 의도적으로 미기록(NET-NEW 판별력 보존 — acceptance.md §D.6). `claude plugin validate --strict`(SHOULD) 미실행 — M6 소관.

**Residual-risk**: 본 저장소 T3 공존 typed-name 충돌(P0-8) 실측은 M6. M1은 개명 + manifest 갱신만 수행; 플러그인 본문(스킬·커맨드)의 잔존 `moai-coder` 참조 35곳(12파일)은 M5 소관(AC-MV2-005a) — M1에서는 스코프 외.


### M2 — 2계층 재배치 (AC-MV2-002a·b·c·d·e·f)

**Claim**: rules 61파일 `rules/moai/` → `templates/claude/rules/moai/` 이동(git mv, R100 0-content-change), ADK 정본 CLAUDE.md vendor + parity-source 마커, settings.project.json Web-activation 3키, `.moai/config/sections` ≥27 yaml vendor + 최소 토큰화, output-styles 2종 플러그인 네이티브 보존.

**Evidence (verbatim AC outputs, 2026-07-09)**:

AC-MV2-002a (NET-NEW+REMOVAL):
```
$ find plugins/moai/templates/claude/rules/moai -type f | wc -l
61
$ test ! -d plugins/moai/rules; echo "exit=$?"
exit=0
```

AC-MV2-002b (PRESERVE — git mv R100 rename detection, self-pass 의도됨):
```
$ git diff --stat -M100 56f9e09..ad86a50 -- 'plugins/moai/rules' 'plugins/moai/templates/claude/rules'
61 files changed, 0 insertions(+), 0 deletions(-)
$ git diff -M100 --summary (...) | grep -c '^ rename'
61   (전부 100% similarity)
$ git diff --numstat -M100 (...) | awk '{a+=$1;d+=$2} END{print a,d}'
0 0   (content-change 라인 0)
```
주: M2 커밋 전 staged-diff로 캡처 — e6b8507(BOOTSTRAP 병렬 세션)이 `plugins/moai/rules` 0파일 터치(비중첩 확인) → post-commit `56f9e09..ad86a50` diff와 동일.

AC-MV2-002c (NET-NEW — EC-6 ADK 정본 판별):
```
$ test -f plugins/moai/templates/CLAUDE.md; echo "exit=$?"
exit=0
$ grep -c 'parity-source: internal/template/templates/CLAUDE.md' plugins/moai/templates/CLAUDE.md
1
$ wc -l plugins/moai/templates/CLAUDE.md
321 plugins/moai/templates/CLAUDE.md   (ADK 정본 319행 + 증명 마커 2행)
$ grep -c 'claude.mo.ai.kr' plugins/moai/templates/CLAUDE.md
0   (anti-pattern 가드: 루트 CLAUDE.md 프로젝트 고유 참조 부재 → ADK 정본 확인)
```
→ parity-source 마커가 유일 기계 판별자(acceptance.md EC-6). ADK 원천 `/Users/goos/moai/moai-adk-go/internal/template/templates/CLAUDE.md`에서 vendor.

AC-MV2-002d (NET-NEW — Web-activation 3키):
```
$ jq -r '.outputStyle' plugins/moai/templates/claude/settings.project.json
moai:MoAI
$ jq '.extraKnownMarketplaces["moai-claude"]' plugins/moai/templates/claude/settings.project.json
{
  "source": "github://modu-ai/claude"
}   (≠ null)
$ jq '.enabledPlugins["moai@moai-claude"]' plugins/moai/templates/claude/settings.project.json
true
$ jq empty plugins/moai/templates/claude/settings.project.json; echo "exit=$?"
exit=0   (valid JSON)
```

AC-MV2-002e (NET-NEW — config sections ≥27 + 최소 토큰화):
```
$ find plugins/moai/templates/moai/config/sections -name '*.yaml' | wc -l
27   (≥27 PASS)
$ grep -c '{{PROJECT_USER_NAME}}' plugins/moai/templates/moai/config/sections/user.yaml
1
$ grep -c '{{PROJECT_NAME}}' plugins/moai/templates/moai/config/sections/project.yaml
1
$ grep -c '{{DATE}}' plugins/moai/templates/moai/config/sections/project.yaml
1
```
토큰화 범위(REQ-MV2-007(c)): 프로젝트-변수 값만 → `{{PROJECT_USER_NAME}}`·`{{PROJECT_NAME}}`·`{{DATE}}`(scaffold.sh M4 3토큰과 일치). 방법론 기본값(development_mode·quality 임계·harness level 등)은 리터럴 보존. 절대경로/머신고유값 0건(사전 스캔 확인). 원천 `.moai/config/sections/` 원본은 무수정(C-2 단방향 vendor).

AC-MV2-002f (PRESERVE — output-styles 플러그인 네이티브 잔류, self-pass 의도됨):
```
$ find plugins/moai/output-styles -maxdepth 1 -type f | wc -l
2   (einstein.md, moai.md)
$ grep -c '^name: MoAI' plugins/moai/output-styles/moai.md
1
```
→ 셀렉터 `moai:MoAI` 계약(research.md §B P0-2) 보존 — M2에서 output-styles 무편집.

**Baseline-attribution**: 기준선 HEAD e6b8507(M1 완료 후 + BOOTSTRAP 병렬 세션 비중첩 커밋). rules 61파일은 M1 커밋 56f9e09에서 `plugins/moai/rules/moai/`에 존재 → M2 git mv로 `templates/claude/rules/moai/` 이동(R100, 0 content-change). CLAUDE.md·settings·config는 HEAD에서 부재(NET-NEW) → M2 산출. output-styles 2종은 M1 기준선과 동일(PRESERVE 회귀 가드).

**Gaps**: scaffold.sh 산출(`{{TOKEN}}` 치환·백업·settings 병합)은 M4 소관(AC-MV2-004a~g) — M2는 템플릿 페이로드 준비까지만. settings.project.json의 `extraKnownMarketplaces` source 포맷(`github://modu-ai/claude`)은 M4 scaffold·P0-w(Web 실측)에서 런타임 검증 대기 — 본 SPEC Out of Scope이나 포맷 적합성은 사용자 실측에 귀속.

**Residual-risk**: templates/CLAUDE.md는 ADK 정본의 스냅샷 — ADK 원본이 갱신되면 templates 사본은 stale(drift 위험). 다만 parity-source 마커가 원천 경로를 명시해 추적 가능. config sections 토큰화는 최소 3종(`{{PROJECT_NAME}}`·`{{VERSION}}`(미사용)·`{{DATE}}` + `{{PROJECT_USER_NAME}}`) — M4 scaffold.sh가 3토큰(PROJECT_NAME/VERSION/DATE)을 치환하므로 `{{PROJECT_USER_NAME}}`은 scaffold 후 리터럴 잔류 가능(M4에서 토큰 세트 확장 여부 소관).


### M3 — 훅 통합 (AC-MV2-003a·b·c·d·e)

**Claim**: hooks 24스크립트(handle-* 20 + 게이트 4) → 단일 `hooks/dispatch.sh` + `hooks/gates/` 5종(기존 4 이관 + gateguard vendor DP-2)로 통합. hooks.json 20 이벤트 전부 dispatch.sh 라우팅, handle-* 20종 삭제, `$CLAUDE_CODE_REMOTE` 분기 + `command -v moai` T3 자동활성 + fail-open(exit 0 전 경로). event 집합 20종 보존(PRESERVE).

**Evidence (verbatim AC outputs, 2026-07-09)**:

AC-MV2-003a (NET-NEW — dispatch.sh 존재 + lint):
```
$ test -f plugins/moai/hooks/dispatch.sh && bash -n plugins/moai/hooks/dispatch.sh; echo "exit=$?"
exit=0
```

AC-MV2-003b (REMOVAL — handle-* 20종 소거):
```
$ find plugins/moai/hooks -name 'handle-*.sh' | wc -l
0
```

AC-MV2-003c (NET-NEW+PRESERVE — 전 이벤트 dispatch.sh 라우팅 + 이벤트 집합 보존):
```
$ jq -r '(.hooks // .) | .. | .command? // empty' plugins/moai/hooks/hooks.json | grep -vc 'dispatch.sh'
0   (20개 command 전부 dispatch.sh — dispatch.sh 외 참조 0)
$ jq -r '(.hooks // .) | if type=="object" then (if has("hooks") then (.hooks|keys[]) else keys[] end) else . end' plugins/moai/hooks/hooks.json | sort > /tmp/m3_events_after.txt
$ diff /tmp/m3_events_before.txt /tmp/m3_events_after.txt
(빈 diff = 이벤트 키 집합 20종 동일 — PRESERVE 회귀 가드 통과)
```
이벤트 키 20종(동일): ConfigChange, CwdChanged, FileChanged, InstructionsLoaded, PermissionDenied, PermissionRequest, PostCompact, PostToolUse, PostToolUseFailure, PreCompact, PreToolUse, SessionEnd, SessionStart, Stop, StopFailure, SubagentStart, SubagentStop, TaskCompleted, TeammateIdle, UserPromptSubmit.

AC-MV2-003d (NET-NEW — dispatch.sh 분기 마커):
```
$ grep -c 'CLAUDE_CODE_REMOTE' plugins/moai/hooks/dispatch.sh
3   (≥1 — Web/remote 분기 + 주석)
$ grep -c 'command -v moai' plugins/moai/hooks/dispatch.sh
1   (≥1 — T3 자동활성 프로브)
$ tail -5 plugins/moai/hooks/dispatch.sh | grep -c 'exit 0'
1   (≥1 — 최종 fail-open exit 0)
```

AC-MV2-003e (NET-NEW — gates ≥5 + lint, DP-2 gateguard vendor 채택):
```
$ ls plugins/moai/hooks/gates/*.sh | wc -l
5
$ for f in plugins/moai/hooks/gates/*.sh; do bash -n "$f" || echo "FAIL $f"; done
(전부 OK — gateguard-fact-force, iggda-audit-preservation-guard, status-transition-ownership, sync-phase-quality-gate, team-ac-verify)
```
gates/ 5종 = 기존 4종(git mv R100 content-intact) + gateguard-fact-force.sh(DP-2 vendor, 원천 `moai-adk-go/internal/template/templates/.claude/hooks/moai/gateguard-fact-force.sh`).

**dispatch.sh event→gate 매핑 (인코딩된 라우팅)**:
- T3 경로(`command -v moai` 성공, `$CLAUDE_CODE_REMOTE != true`): PascalCase→kebab 변환 후 `exec moai hook <kebab>` — 20 이벤트 전부 매핑(PreCompact→`compact` 특수케이스 포함). T3에서 moai native가 전담, bash 게이트는 미실행(설계 의도 — T1/T2/Web 대비 fallback).
- Gate-only fallback(바이너리 부재 / Web remote): PostToolUse→`status-transition-ownership.sh`, Stop→`sync-phase-quality-gate.sh`, TaskCompleted→`team-ac-verify.sh`, PreToolUse→`gateguard-fact-force.sh`(DP-2 vendor). iggda-audit-preservation-guard.sh는 이벤트 매핑 없음(수동/orchestrator 검증배치 호출 전용 — 헤더 "Run: bash ..." 명시).
- 매핑 없는 16종 이벤트(SessionStart, PreCompact, SessionEnd, PostToolUseFailure, SubagentStart, SubagentStop, UserPromptSubmit, TeammateIdle, ConfigChange, StopFailure, PostCompact, InstructionsLoaded, CwdChanged, FileChanged, PermissionDenied, PermissionRequest) → 무음 `exit 0`(retired handle-* stub 동질 — stdin drain + fail-open).

**기능 smoke test (T3 환경 — 본 저장소 moai 바이너리 존재)**:
```
$ echo '{...PostToolUse...}' | bash dispatch.sh PostToolUse
{"hookSpecificOutput":{"hookEventName":"PostToolUse"}}   ← exec moai hook post-tool 정상 동작
$ CLAUDE_CODE_REMOTE=true bash dispatch.sh PostToolUse   ← gate-only 모드 분기 확인(status-transition-ownership 게이트 실행)
$ CLAUDE_CODE_REMOTE=true bash dispatch.sh SessionEnd < /dev/null; echo "exit=$?"
exit=0   ← 매핑 없음 → drain + fail-open
```

**Baseline-attribution**: 기준선 HEAD 3dfcc42(병렬 PM-REDESIGN 세션 커밋 흡수 — plugins/moai/ 비중첩 확인). M3 착수 전: handle-* 20 + 게이트 4 = .sh 24종, hooks.json 20 이벤트가 handle-*.sh(20)+게이트(2: status-transition PostToolUse, sync-phase Stop)로 분산. M3 후: dispatch.sh 1 + gates/ 5 = 구조 통합, 이벤트 집합 20종 불변(PRESERVE). 게이트 4종은 git mv R100(content-intact, 내부 로직 무편집 — B10). gateguard는 ADK 정본에서 vendor(DP-2, parity-source 동일 경로).

**Gaps**: 본 저장소 T3 환경에서 `exec moai hook` 경로가 바이너리 감지 시 게이트를 우회하는 것은 설계 의도(T3 native 전담)이나, moai native hook이 4 bash 게이트(status-transition-ownership 등)의 등가 기능을 포함하는지는 M6 런타임 검증(AC-MV2-006a~d) 소관. gateguard(PreToolUse→첫편집 조사 advisory)는 additive 동작 — 기존 handle-pre-tool.sh(pure stub) 대비 advisory 추가, 단 fail-open(exit 0) 불변. iggda-audit-preservation-guard.sh는 이벤트 매핑 없음(수동 호출 전용) — gates/에 존재하나 dispatch.sh 라우팅 미연결(현행 hooks.json에서도 미연결이었으므로 PRESERVE).

**Residual-risk**: dispatch.sh의 PascalCase→kebab 변환표는 moai 바이너리 서브커맨드 명명 규칙에 의존 — moai CLI가 서브커맨드명을 변경하면 변환표 갱신 필요(현재 20종 전부 ADK handle-*.sh.tmpl 원천과 교차 검증 완료). `$CLAUDE_CODE_REMOTE` 분기는 Web 세션에서 바이너리 프로브를 생략(REQ-MV2-011)하나, 실제 Web 환경($CLAUDE_CODE_REMOTE=true)에서의 게이트 동작 검증은 P0-w(사용자 수행, §E Out of Scope) 대기. 클라ude plugin validate exit 0(warnings = pre-existing command frontmatter 경고, M1 기준선과 동일 — 회귀 아님).

## §E.3 Run-phase Audit-Ready Signal

_<pending run-phase>_

## §E.4 Sync-phase Audit-Ready Signal

_<pending sync-phase — manager-docs 기록 영역 (sync_commit_sha)>_
