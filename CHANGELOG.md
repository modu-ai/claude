# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added — SPEC-MOC-PLUGIN-MOAI-V2-001

moai plugin v2 — rename (`moai-coder` → `moai`, clean-slate version `1.0.0` per user decision DP-1), two-layer restructure (`rules/` → `templates/claude/`), single-dispatcher hook consolidation, and deterministic scaffolding via `/moai:project`. Establishes the Web-tier activation contract (marketplace + output-style selector + enabled-plugin) and completes the v2 redesign P2 phase for this repository's owned portion.

**Core deliverables**:
- **M1** — `git mv plugins/moai-coder → plugins/moai` + `plugin.json` (`name: moai`, `displayName: 코더`, `version: "1.0.0"`) + marketplace.json 4-plugin entry (moai-coder tombstone removed) (AC-MV2-001a/b/c/d)
- **M2** — two-layer restructure: `rules/moai/` → `templates/claude/rules/moai/` (61 files, 100% git rename R100, 0 content change) + ADK-upstream `templates/CLAUDE.md` (parity-source marker) + `templates/claude/settings.project.json` (Web-activation 3 keys: `outputStyle: moai:MoAI`, marketplace `moai-claude`, enabled `moai@moai-claude`) + `templates/moai/config/sections/*.yaml` (27 token-holders) (AC-MV2-002a~f)
- **M3** — hook consolidation: single `hooks/dispatch.sh` (fan-in for all 20 events, `$CLAUDE_CODE_REMOTE` branch + `command -v moai` T3 auto-activation + fail-open `exit 0`) + `hooks/gates/` 5 scripts (4 migrated + gateguard-fact-force vendor per DP-2); 20 `handle-*.sh` scripts removed (AC-MV2-003a~e)
- **M4** — `scripts/scaffold.sh` (deterministic cp+sed scaffolder, `--dry-run`, backup, user-owned preservation, settings.json merge preservation) wired into `/moai:project` skill; Layer-2 template payload deployable to arbitrary target projects (AC-MV2-004a~g)
- **M5** — reference sweep: `moai-coder` references in `plugins/` → 0 (was 35/12 files), `www/content/plugins/**` old-name (`moai-code`/`moai-coder`) → 0 (was 17/5 files) + `moai@moai-claude` added, root `README.md` 4-plugin topology, `plugins/moai/README.md` reinstall notice (AC-MV2-005a~f)
- **M6** — verification + P0-8 typed-name measurement: `claude plugin validate` ×2 PASS, `bash -n` 7 scripts PASS, Hugo build 228p PASS; P0-8 verdict recorded (probe-layer indeterminate — 13 project/plugin command names genuinely collide; deactivation-guidance UI is P3 out-of-scope) (AC-MV2-006a~d)

**Verification**: 32/32 AC PASS (AC-MV2-006d link-check PASS-WITH-DEBT — 10 pre-existing broken links in cookbook/cowork/tags, NOT a regression; `--strict` validate exit 1 is SHOULD debt EC-5). Run-phase commits: `56f9e09` (M1) → `ad86a50` (M2) → `7ff8c5f` (M3) → `21fb72c` (M4) → `5037668` (M5) → `6e0ccdc` (M6).

**Key files**:
- `plugins/moai/` (renamed from `plugins/moai-coder/`; manifest, templates/, hooks/, scripts/scaffold.sh)
- `plugins/moai/hooks/dispatch.sh` (new — single event dispatcher, `@MX:ANCHOR`)
- `plugins/moai/scripts/scaffold.sh` (new — deterministic Layer-2 scaffolder, `@MX:ANCHOR`)
- `plugins/moai/templates/{CLAUDE.md, claude/rules/moai/, claude/settings.project.json, moai/config/sections/}` (new two-layer payload)
- `.claude-plugin/marketplace.json` (moai entry replaces moai-coder tombstone)
- `www/content/plugins/{_index,code/_index,chat/_index,cowork/_index,design/_index}.md` (catalog rename)
- Root `README.md` (4-plugin topology)

**Residual debt**: (1) `--strict` plugin validate exit 1 — 12 command frontmatter gaps (EC-5, follow-up frontmatter SPEC); (2) www link-check 10 pre-existing broken links (cookbook/cowork/tags — separate SPEC); (3) P0-8 typed-name deactivation-guidance UI not implemented (P3 out-of-scope).

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

### Added — SPEC-MOC-PLUGIN-STORY-001

moai-story 플러그인 신설 + 패밀리 v4 재배치 — 작가 도메인 전용 플러그인(21스킬: 이관 8 + 신규 13) + Higgsfield MCP 연동 + cowork v4.0.0 마이그레이션.

**Core deliverables**:
- **M1** — moai-story 스캐폴딩 (plugin.json v0.1.0, .mcp.json higgsfield canonical, skills/)
- **M2** — 이관 스킬 8종 복사 (cowork → story) + book-revision-coach fallback note
- **M3** — 신규 스킬 13종 작성 (story-*) + 위생 스윕프 (3rd-person/무엇을-언제/AI-tell across all 21)
- **M4** — cowork v4.0.0 마이그레이션 (book-* 8스킬 제거, higgsfield MCP 제거, 171 SKILL.md 4.0.0, CHANGELOG v4.0.0)
- **M5** — marketplace.json 4플러그인 엔트리 (moai-story 추가, metadata.version 4.0.0, per-entry version 미기재)
- **M5-fix** — moai-story author string→object 정정 (Claude Code plugin schema)
- **M6** — www 문서 갱신 (index/migration/higgsfield-setup/CHANGELOG + content/_index.md live-site update)

**Verification**:
- 10/12 AC PASS (AC-001~010 full/intent PASS; AC-011 PASS-WITH-DEBT --strict structural; AC-012 PASS-WITH-DEBT count drift ND5)
- ND debt: ND3/4/5/6/7/8 resolved (pre-fixed + sync-phase acceptance.md cleanup); ND1/2 resolved (plan-phase); ND9 residual (non-blocking, pre-existing warnings + SPEC-required category)
- DRIFT-001 depends_on noted: DRIFT-001 not yet created, but run-phase accepted `status: in-progress` per M0 gate policy; sync non-blocking
- Hugo build: exit 0, dead-link check 0
- Run-phase commits: `76741dc` (M1) → `105175e` (M2) → `cabbdb1` (M3) → `d1d5887` (M4) → `8629c5d` (M5) → `5dfe2d4` (M5-fix) → `11f7379` (M6)

**Files modified**:
- `plugins/moai-story/` (NEW PLUGIN — plugin.json, .mcp.json, skills/ 21개)
- `plugins/moai-cowork/` (v4.0.0 — 8 book-* 스킬 제거, higgsfield MCP 제거, 171 SKILL.md 4.0.0, CHANGELOG)
- `.claude-plugin/marketplace.json` (4플러그인 엔트리, metadata.version 4.0.0)
- `www/plugins/{index,migration,higgsfield-setup}.md` + `www/CHANGELOG.md` (문서 갱신)

**Residual**: ND9 — AC-STORY-011 `claude plugin validate . --strict` fails on pre-existing warnings (metadata.language, metadata.license) + SPEC-required category field (structural conflict); non-strict validate exits 0.

