# SPEC-MOC-SITE-IA-001 — Progress

- **SPEC ID**: SPEC-MOC-SITE-IA-001
- **Tier**: L (proposed)
- **Status**: draft (plan-phase artifacts created)
- **Phase**: plan-phase AUDITED (iter-2 PASS 0.90 @ e0e31d2, 2026-07-04) + Implementation Kickoff approved (Option 1) → run-phase entry

## §E.1 Plan-phase Audit-Ready Signal

- **plan_complete_at**: 2026-07-02
- **plan_status**: audit-ready
- **Artifacts created (4)**: `spec.md` (GEARS REQ-IA-001..024, §E Out of Scope 6 H3 sub-sections), `plan.md` (M1-M6 priority-based, R3 gated on SPEC-MOC-PLUGIN-REMEDIATION-001), `acceptance.md` (AC-IA-001..024 + 6 GWT + 6 edge cases + DoD), `progress.md` (this file).
- **Frontmatter self-check**: 12 canonical fields present; `id` matches `^SPEC(-[A-Z][A-Z0-9]*)+-\d{3}$` (decomposition SPEC|MOC|SITE|IA|001 → PASS); `created`/`updated`/`tags` canonical names; optional `tier`/`depends_on`/`related_specs` included.
- **Out of Scope lint**: §E carries literal "out of scope" + 6× `### Out of Scope — <topic>` H3 sub-headings each with `-` bullets (satisfies OutOfScopeRule).
- **Scope**: `www/**` only. `plugins/**` source excluded (owned by REMEDIATION-001 / BOOTSTRAP-DESKTOP-001).
- **Known dependencies (cleared 2026-07-03)**: SPEC-MOC-PLUGIN-REMEDIATION-001 = implemented (R3/M5 gate cleared), SPEC-MOC-BOOTSTRAP-DESKTOP-001 = implemented (R4/M4 Tier 1~3 bridge available).
- **Baseline (measured 2026-07-02)**: 178 content md / 11 flat sections; mermaid 139/178; aliases precedent 10p; design≈claude-design near-dup; plugins 33p obsolete; `/cli` absent; CLI source 13 ko sections present.

- **Plan-audit verdict (2026-07-04, iter-2)**: PASS 0.90 (Tier L thresh 0.85, skip-eligible ≥0.90). MP-1..4 PASS (MP-2 GEARS borderline resolved via D3 anchors). iter-1 0.85 → iter-2 0.90 monotonic, no regression vs prior-session iter-3 0.90. Reports: `.moai/reports/plan-audit/SPEC-MOC-SITE-IA-001-2026-07-{03,04}.md`. Resolved: D3/D5/D6. Documented debt (sync): D1 lean Tier-L / D2 REQ-024 placement / D4 qualitative ACs. Non-blocking new: D7 (AC-011 verify-cmd, MINOR) / D8 (stale iter-3 label, COSMETIC).

## §E.2 Run-phase Evidence

_<pending run-phase — owned by manager-develop>_

## §E.3 Run-phase Audit-Ready Signal

_<pending run-phase — owned by manager-develop>_

## §E.4 Sync-phase Audit-Ready Signal

_<pending sync-phase — owned by manager-docs>_

## §E.5 Mx-phase Audit-Ready Signal

_<pending Mx-phase — owned by manager-docs / orchestrator>_

## §E.6 Phase 0.95 Mode Selection

- **Input parameters**: tier=L · scope≈30+ files (menu SSOT + CLI ~25-30 new pages + plugin rewrite + DESIGN merge + source-index) · domains=6 (menu/DESIGN/help-office/CLI-content/plugins/link-checker-tooling) · language=100% markdown + 1 Node script · concurrency-benefit=LOW (content-authoring heavy, shared files across milestones) · Agent-Teams-prereqs=not-met
- **Decision: Mode 5 (sub-agent)** — sequential milestone delegation
- **Justification**: Tier L + markdown/content-authoring heavy (per-page creative, not mechanical-uniform) → Mode 6 (workflow) excluded per Anthropic coding-heavy caveat. Shared files (menu `main.yaml`, `source-index.md`) across M1/M3/M5/M6 preclude safe parallel (Mode 4). §B.2 "Tier L + markdown/shell-only → Mode 5 with Section A-E template". Implementation Kickoff approved (Option 1) + plan-audit PASS 0.90 → Mode 5 entry conditions met.
- **Milestone grouping (sequential delegations)**: D₁ = M1+M2+M3 (structural core) · D₂ = M4 (CLI, largest) · D₃ = M5 (plugins, REMEDIATION-001 gate cleared) · D₄ = M6 (finalization).
