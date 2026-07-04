# SPEC-MOC-SITE-IA-001 — Progress

- **SPEC ID**: SPEC-MOC-SITE-IA-001
- **Tier**: L (proposed)
- **Status**: draft (plan-phase artifacts created)
- **Phase**: plan-phase complete → awaiting plan-audit + Implementation Kickoff Approval

## §E.1 Plan-phase Audit-Ready Signal

- **plan_complete_at**: 2026-07-02
- **plan_status**: audit-ready
- **Artifacts created (4)**: `spec.md` (GEARS REQ-IA-001..024, §E Out of Scope 6 H3 sub-sections), `plan.md` (M1-M6 priority-based, R3 gated on SPEC-MOC-PLUGIN-REMEDIATION-001), `acceptance.md` (AC-IA-001..024 + 6 GWT + 6 edge cases + DoD), `progress.md` (this file).
- **Frontmatter self-check**: 12 canonical fields present; `id` matches `^SPEC(-[A-Z][A-Z0-9]*)+-\d{3}$` (decomposition SPEC|MOC|SITE|IA|001 → PASS); `created`/`updated`/`tags` canonical names; optional `tier`/`depends_on`/`related_specs` included.
- **Out of Scope lint**: §E carries literal "out of scope" + 6× `### Out of Scope — <topic>` H3 sub-headings each with `-` bullets (satisfies OutOfScopeRule).
- **Scope**: `www/**` only. `plugins/**` source excluded (owned by REMEDIATION-001 / BOOTSTRAP-DESKTOP-001).
- **Known dependencies (cleared 2026-07-03)**: SPEC-MOC-PLUGIN-REMEDIATION-001 = implemented (R3/M5 gate cleared), SPEC-MOC-BOOTSTRAP-DESKTOP-001 = implemented (R4/M4 Tier 1~3 bridge available).
- **Baseline (measured 2026-07-02)**: 178 content md / 11 flat sections; mermaid 139/178; aliases precedent 10p; design≈claude-design near-dup; plugins 33p obsolete; `/cli` absent; CLI source 13 ko sections present.

## §E.2 Run-phase Evidence

_<pending run-phase — owned by manager-develop>_

## §E.3 Run-phase Audit-Ready Signal

_<pending run-phase — owned by manager-develop>_

## §E.4 Sync-phase Audit-Ready Signal

_<pending sync-phase — owned by manager-docs>_

## §E.5 Mx-phase Audit-Ready Signal

_<pending Mx-phase — owned by manager-docs / orchestrator>_
