# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
