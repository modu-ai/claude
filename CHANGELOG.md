# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added — SPEC-MOC-BOOTSTRAP-DESKTOP-001

Bootstrap architecture + moai-code Desktop Edition capability elevation — defining two-entrypoint parity (`/project init` for non-developers, `/moai:project` for no-install developers) with single canonical source (`internal/template/templates/`). Version stamp SSOT established (4-location release checklist) and version bound from 0.1.0 → 3.0.0 per user decision D1.

**Core deliverables**:
- **M1** — `/project init` folder-convention scaffold + `.moai/skill-profile.yaml` persisted artifact (AC-BD-001a/b/c NET-NEW gates; skill-profile.yaml directive + Phase 6.5/6.6 workflow)
- **M2** — Parity contract documentation + `plugin-deployed vX.Y.Z` stamping directive (AC-BD-003 NET-NEW; parity between `/moai:project` and `moai init` documented)
- **M3** — Desktop Edition Tier 1-3 capability table + session-start binary detection branch + fail-open preservation (AC-BD-004/005a/b; Tier 1/2/3 structure + hook split)
- **M4** — VERSION-SSOT release checklist sentinel + D1 version bind 0.1.0 → 3.0.0 (AC-BD-006c NET-NEW, AC-BD-006d D1-GATED; 3-location normalized literal match)
- **M5** — SKIPPED per user decision D2=KEEP (displayName unchanged; AC-BD-007 OPTION not activated)

**Verification**:
- 11/12 static AC PASS (M1-M4 comprehensive; V12 RUNTIME AC-002/003-runtime documented as residual risk — require `/moai:project` plugin-command execution for full runtime verification, out of sync-phase scope)
- Preserved 4 invariants (legacy alias 14, CLAUDE.md heading 1, exit 0=1, {{.Version}}=2, parity-source markers=12)
- Version bind applied: moai-cowork/moai-code plugin.json both `3.0.0` (binds to binary v3.0.x line per REQ-BD-012)
- Run-phase commits: `e0b7b37` (M1) → `e43674e` (M2) → `22e09d4` (M3) → `570ed6b` (M4)

**Files modified**:
- `plugins/moai-cowork/skills/project/SKILL.md` (Phase 6.5/6.6 workflow, folder scaffold, skill-profile directive, EC6 distinction)
- `plugins/moai-code/README.md` (Desktop Edition Tier table, parity contract, VERSION-SSOT section)
- `plugins/moai-code/hooks/moai/handle-session-start.sh` (binary detection branch, Tier 3 promotion notice)
- `plugins/moai-cowork/.claude-plugin/plugin.json` (version `3.0.0`)
- `plugins/moai-code/.claude-plugin/plugin.json` (version `3.0.0`)

**Residual**: V12 RUNTIME AC (AC-BD-002, AC-BD-003-runtime) documented as residual risk — require `/moai:project` plugin-command execution in environment with `moai` binary available for full runtime verification.

### Added — SPEC-MOC-PLUGIN-REMEDIATION-001

Korean-slop remediation across 177 cowork + 11 design skills (gate structure, decontamination, namespace normalization, boundary dedup, lint CI), plus Phase A category-prefix rename of 150 skills (148 prefix-add + 2 body-rename, 26 no-op) per approved §D.9 mapping.

**Core deliverables**:
- P0 gate structure + P2 immediate-failure path repair (AC-001..007)
- P1 decontamination of 50 copy sources (slide/deck samples, commerce/newsletter boilerplate, dash-contrast headlines)
- P3 gate wiring (8 priority skills + project router)
- P2 bulk repair: 9 deprecated namespaces normalized across 70 files, project router rewritten for single-plugin architecture, stale refs repaired, ghost dir removed (AC-015..017)
- Phase A rename: 150 skills renamed with category prefixes (commerce-/content-/marketing-/media-/finance-/book-/legal-/education-/business-/office-/general-) — 0 dangling old-name references verified (AC-018)
- Phase B dedup: design-system-library cowork copy → pointer, brand-identity scope narrowed (AC-019..020)
- P4 re-occurrence prevention: skill-builder Korean authoring rules, lint CI script (korean-slop-lint.sh) with 4-class self-test, scope discipline (AC-021..024)

**Verification**:
- 24/24 AC PASS (all MUST-PASS + SHOULD-PASS criteria satisfied)
- AC-018 resolved via standalone-reference interpretation (§D.9.5): residual word-boundary matches are legitimate new-name substrings, URLs, genre enums, cross-plugin pointers — 0 actual dangling references
- Run-phase commits: `b7ca913` (M1) → `665bbb3` (M2-M5-Phase-B) → `f44bb47` (M5-Phase-A AC-018 rename)
- www/plugins/ re-sync required (owned by SPEC-MOC-SITE-IA-001 — REQ-REM-024)

**Files modified**: ~25-40 source files across plugins/moai-cowork/skills/, plugins/moai-design/skills/, scripts/, skill-builder/, marketplace.json, llms.txt (M1-M6 cumulative)

**Residual**: moai-core namespace flagged by AC-015 grep but exempt per plan.md §A.5 (separate SPEC ownership)
