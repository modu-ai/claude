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

## §E.2 Run-phase Evidence

_<pending run-phase — populated by manager-develop>_

## §E.3 Run-phase Audit-Ready Signal

_<pending run-phase — populated by manager-develop>_

## §E.4 Sync-phase Audit-Ready Signal

_<pending sync-phase — populated by manager-docs>_

## §E.5 Mx-phase Audit-Ready Signal

_<pending Mx-phase>_
