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


## §E.3 Run-phase Audit-Ready Signal

_<pending run-phase>_

## §E.4 Sync-phase Audit-Ready Signal

_<pending sync-phase — manager-docs 기록 영역 (sync_commit_sha)>_
