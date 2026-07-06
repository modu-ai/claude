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

### Added — SPEC-MOC-SITE-IA-001

사이트 정보 구조(IA) 2축 재편 (데스크탱/CLI) + DESIGN 병합 완료 + 플러그인 문서 4 카테고리 현행화 + CLI 축 신규 콘텐츠 22페이지 + 내부링크 체커 도구 신규.

**Core deliverables**:
- **D₁ (M1+M2+M3)** — 메뉴 SSOT 2축 재편: 데스크탑 축(🖥️) / CLI 축(⌨️) / 공통 하단(도움말·쿡북·실전 트랙·릴리스). DESIGN 병합 완료(`claude-design/` 디렉토리 삭제 + alias 10건 보존). help/office 통합(office→도움말 2p 이동 + alias). cookbook/tracks 메뉴 중복 제거.
- **D₂ (M4)** — CLI 축 신규 콘텐츠 22페이지: 시작하기(3p) + 핵심 개념(5p) + 일상 사용(5p) + MoAI-ADK(4p) + 레퍼런스(4p) + `_index.md`(5p). moai-adk-go 원문을 입문자 친화적 한국어 prose-first로 재저작. PLAN→RUN→SYNC stateDiagram 포함.
- **D₃ (M5)** — 플러그인 문서 4 카테고리 재편: chat(문서 허브) / cowork(177스킬) / design(11스킬) / code(13명령+7에이전트+28스킬). marketplace.json 3 플러그인 현실 반영. 구 33 obsolete page → alias 리다이렉트(38건).
- **D₄ (M6)** — source-index CLI 축 확장("다루지 않" 제한 문구 제거 4→0건, `/cli/` 경로 참조 0→28건) + 전용 내부링크 체커(`www/scripts/check-links.mjs`) 신규.

**Verification**:
- 23/24 AC PASS (AC-IA-001..022, 024 — structural delta + per-page alias + Hugo build exit 0)
- AC-IA-023 PASS-WITH-DEBT — 전용 링크체커가 pre-existing broken internal links 10건 발견(cookbook 본문 상대경로 오타 5건 + Hugo taxonomy 렌더링 한계 5건, commit 6d78fbf부터 기원). **SPEC 산출 콘텐츠(cli/**, plugins/{chat,cowork,design,code}/**, help/source-index.md)에서 broken 0건** — 전부 out-of-scope PRESERVE 대상. 별도 후속 SPEC에서 정비.
- Hugo build: exit 0, 228 pages, 65 aliases, 392 ms (M6 finalization rebuild)
- 전용 링크체커: `node www/scripts/check-links.mjs www/public` → exit 1, `broken internal links: 10` (전부 pre-existing; SPEC-produced content 0건)

**Files modified**:
- `www/data/menu/main.yaml` (2축 재편 + axis 마커)
- `www/content/cli/**` (22 신규 페이지 — 5 섹션)
- `www/content/plugins/{_index,chat,cowork,design,code}/_index.md` (4 카테고리 재편 + 5 공통 스켈레톤)
- `www/content/help/source-index.md` (CLI 축 확장)
- `www/scripts/check-links.mjs` (신규 204행 Node script — AC-IA-023 권威 체커)
- `content/claude-design/` 디렉토리 삭제 (DESIGN 병합 완료)
- 구 33 plugin 페이지 → alias 리다이렉트 처리

**Run-phase commits**:
- D₁: `a803537`, `e50dc6e`, `d3d139e`
- D₂: `21e44dc`, `109dba7`, `4645bb2`, `4834643`, `f6c6750`, `12eaa8e`
- D₃: `637e1cd`, `aa35d8c`, `93c4871`, `4a56289`, `52d9072`, `5a37229`
- D₄: `7771497`, `2e7353c`, `c6c7aed` (이 커밋)

**Residual**: AC-IA-023 pre-existing broken internal links 10건 (cookbook 본문 5건 + Hugo taxonomy 5건) — 별도 후속 SPEC에서 정비. SPEC 산출 콘텐츠는 모든 내부링크 정상(0 broken).
