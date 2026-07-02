# SPEC-MOC-PLUGIN-REMEDIATION-001 — Progress

## §E.1 Plan-phase Audit-Ready Signal

Plan-phase artifacts (spec.md, plan.md, acceptance.md, progress.md) authored by manager-spec on 2026-07-02. Evidence base: the 3-way cross-verified Korean AI-tell audit persisted in auto-memory `project_plugin_korean_slop_audit.md` (origin session `28305de2`), plus **independent live re-verification of every target path against the `plugins/` tree at authoring time** (not trusted from the secondhand audit summary) per `.claude/rules/moai/core/verification-claim-integrity.md`. Re-verification surfaced count drift from the audit's frozen numbers (cowork 177 not 178; deprecated-ns 68 not 78; design 11 confirmed) — recorded in spec.md §A.3 — which is why all 24 acceptance criteria are re-runnable end-state predicates, not frozen counts.

- **Requirements**: 24 (REQ-REM-001..024, GEARS: Ubiquitous / Event-driven / Unwanted / Where).
- **Acceptance criteria**: 24 (AC-REM-001..024, full 1:1 REQ↔AC traceability, 5 GWT scenarios, 6 edge cases).
- **Tier**: L (constitutional-scale; PASS threshold 0.85). NOTE: delivered as the 3-file core + this progress.md; conventional Tier-L design.md/research.md folded into spec.md §A.2/§A.3 + plan.md §F (extractable if plan-auditor requires the 5-artifact set).
- **Milestones**: M1 (P0 gate structure + P2 immediate-failures, RELEASE-BLOCKING) → M2 (P1 decontamination) → M3 (P3 gate wiring) → M4 (P2 bulk repair) → M5 (Phase A rename + Phase B dedup) → M6 (P4 lint CI + re-sync note).
- **Scope**: owns `plugins/moai-cowork/skills/**`, `plugins/moai-design/skills/**`, `plugins/{moai-cowork,moai-design}/scripts/**`, skill-builder. Excludes moai-code, commands, templates (SPEC-MOC-BOOTSTRAP-DESKTOP-001), www (SPEC-MOC-SITE-IA-001).
- **www/plugins/ re-sync**: required after source edits, owned by SITE-IA (REQ-REM-024) — recorded here per that requirement.

Ready for plan-auditor independent review (Tier L threshold 0.85).

## §E — Phase 0.95 Mode Selection

**Input parameters**:
- tier: **L** (constitutional-scale; ~188 skill dirs + gates + lint CI)
- scope (file count): ~25-40 source files across M1-M6 (gates, slides, copy sources, router, skill-builder, lint script)
- domain count: 4 (Korean-slop detection/gate content, execution-path repair, namespace/rename mechanics, lint CI scripting)
- file language mix: ~95% Markdown skill bodies + 1 shell lint script (M6)
- concurrency benefit: **LOW** — coding-heavy content edits with sequential inter-file dependency (M4 namespace normalize MUST precede M5 rename; M2 copy edits settle before M5; M1 gate-structure additions referenced by M3 wiring)
- Agent Teams prereqs: not met

**Mode evaluation**:

| # | Mode | Selected? | Rationale |
|---|------|-----------|-----------|
| 1 | trivial | no | Multi-file, multi-milestone, semantic content edits |
| 2 | background | no | Write tasks; background-write forbidden |
| 3 | agent-team | no | Prereqs not met; coding-heavy (Anthropic caveat) |
| 4 | parallel | no | Coding-heavy + sequential inter-file dependency (M4→M5, M1→M3) |
| 5 | sub-agent | **YES** | Tier L + coding-heavy + sequential M1→M6 inter-file dependency |
| 6 | workflow | no | Not a single uniform mechanical transform; semantic reference-coupled edits |

**Decision**: `sub-agent` (Mode 5 — sequential, single implementer, no spawn).

**Justification**: Per Anthropic's coding-task parallelism caveat, this SPEC's milestones have strong sequential coupling: M1 gate-structure additions define the patterns M3 wiring references; M2 copy edits settle before M5 rename; M4 namespace normalization MUST precede M5 rename (EC-4); M6 lint CI runs last against final names. Mode 6 requires a single uniform mechanical transform with no inter-file dependency — this SPEC's edits are semantic (Korean copy decontamination, gate-structure authoring, genre-profile definition) and reference-coupled. Mode 5 sequential is the correct default.

## §E.2 Run-phase Evidence

### Re-baseline (run-phase pre-flight, 2026-07-02)

Live counts re-measured at run-phase start, compared against `spec.md` §A.3 plan-phase numbers. Per EC-1, the implementer proceeds against the LIVE numbers.

| Item | Plan-phase (§A.3) | Run-phase LIVE | Drift | Action |
|------|------------------|----------------|-------|--------|
| cowork skills | 177 | **177** | 0 | matches |
| design skills | 11 | **11** | 0 | matches |
| deprecated-namespace files (`grep -rl` 9 ns tokens) | 68 | **72** | +4 | proceed against live 72 (M4 sweeps all) |
| `ai-slop-reviewer` em-dash | 10 | **10** | 0 | AC-012 baseline confirmed |
| `humanize-korean` em-dash | 41 | **41** | 0 | AC-012 baseline confirmed |
| `pdf-writer` `moai-office` path spots | 4 (L56,59,60,95) | **4** (L56,59,60,95) | 0 | AC-006 confirmed |
| `humanize-korean` `moai-content` path | 3 (L73,89,170) | **3** (L73,89,170) | 0 | AC-007 confirmed |
| `live-commerce` deceptive-ad "집중력 200%" | present | **present** (references/live-script.md:79) | 0 | AC-010 confirmed |

**Drift disposition**: deprecated-namespace +4 drift is within the predicate-tolerant design (AC-015 is a `→0` end-state predicate, not a count). No material divergence requiring a blocker report.

### Milestone progress

_<populated per-milestone below as edits land>_

## §E.3 Run-phase Audit-Ready Signal

_<pending — populated by manager-develop on run-phase completion>_

## §E.4 Sync-phase Audit-Ready Signal

_<pending sync-phase — populated by manager-docs>_

## §E.5 Mx-phase Audit-Ready Signal

_<pending Mx-phase>_
