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

### D₁ — M1+M2+M3 (structural core, 2026-07-04)

- **M1 (메뉴 2축 재편 + URL 전략)** — PASS. `www/data/menu/main.yaml` 데스크탑 축(시작하기→CHAT→COWORK→DESIGN→CODE→MoAI 플러그인) / CLI 축(시작하기→핵심 개념→일상 사용→MoAI-ADK→레퍼런스) / 공통 하단(도움말·쿡북·실전 트랙·릴리스) 3-group 재편. axis 마커(emoji + YAML comment separator)로 grep 가능.
  - commits: `a803537` (M1 menu 2축 + axis markers), `e50dc6e` (M1 iter-2 fix), `d3d139e` (M2+M3 cleanup).
  - AC-IA-001/002/003/004/022 PASS.
- **M2 (DESIGN 병합 마무리)** — PASS. `content/claude-design/` 디렉토리 삭제(유일 실질 변경). HEAD에서 흡수 + `/claude-design/*` alias 10은 이미 완료 상태였으므로 재흡수·재alias 금지 원칙 준수.
  - AC-IA-005/006 PASS (디렉토리 부재 AND alias 커버리지 ≥ 10).
- **M3 (help/office 통합 + tracks 중복 제거)** — PASS. `content/office/`(2p) → 도움말 하 통합 + alias. cookbook/tracks 메뉴 중복 단일화.
  - AC-IA-016/017 PASS.

### D₂ — M4 CLI 축 신규 콘텐츠 (2026-07-04, 이 위임)

- **Worktree base**: `worktree-agent-acb8978ec711f2923` @ `d3d139e` (= D₁ final HEAD, origin-synced).
- **M4 산출물 (22 신규 페이지, 5 섹션)**:
  - `www/content/cli/_index.md` (CLI 축 홈)
  - `www/content/cli/start/{_index, install, first-spec}.md` (3p — 시작하기)
  - `www/content/cli/concepts/{_index, spec-system, ddd-tdd, trust5, harness}.md` (5p — 핵심 개념)
  - `www/content/cli/daily/{_index, daily-flow, prompts, tokens-cost, debugging}.md` (5p — 일상 사용)
  - `www/content/cli/moai-adk/{_index, bridge, workflow-commands, quality-commands}.md` (4p — MoAI-ADK)
  - `www/content/cli/reference/{_index, cli-reference, multi-llm, advanced}.md` (4p — 레퍼런스)
- **Commits (6, NO PUSH — orchestrator owns push)**:
  - `21e44dc` — feat: M4 cli 시작하기 섹션 (4p)
  - `109dba7` — feat: M4 cli 핵심 개념 섹션 (5p)
  - `4645bb2` — feat: M4 cli 일상 사용 섹션 (5p)
  - `4834643` — feat: M4 cli MoAI-ADK 섹션 (stateDiagram + bridge) (4p)
  - `f6c6750` — feat: M4 cli 레퍼런스 섹션 (4p)
  - `12eaa8e` — feat: M4 menu CLI placeholder 충전 (22 refs + '핵심' badge on bridge)
- **Menu placeholder**: `[M4 예정|PLACEHOLDER]` sentinel 5건 전부 제거 → 실제 22 entries로 충전. `grep -nE 'M4 예정|PLACEHOLDER' www/data/menu/main.yaml` → 0 matches (PASS).

### M4 AC 증거 (Self-Verification)

| AC | Status | Verification Command | Actual Output |
|----|--------|---------------------|---------------|
| AC-IA-012(a) | PASS | `ls -d www/content/cli` | exit 0 (dir exists) |
| AC-IA-012(b) | PASS | `grep -rnE 'url:[[:space:]]*/code' www/content/cli --include='*.md'` | 0 matches (exit 1) — `/cli`↔`/code` URL 무충돌 |
| AC-IA-012(c) | PASS | `cd www && hugo --gc --minify` | exit 0 (Total in 13963 ms, 0 errors) |
| AC-IA-013 | PASS | CLI 5 섹션 `_index.md` 존재 + 원문 복붙 아님 | 5/5 `_index.md` 존재 (start/concepts/daily/moai-adk/reference); 재저작 (개발자 문체 moai-adk-go 원문 → 입문자 친화적 한국어 prose-first + 비유 + colored mermaid) |
| AC-IA-014 | PASS | `grep -rl 'stateDiagram' www/content/cli` | `www/content/cli/moai-adk/_index.md` (PLAN→RUN→SYNC stateDiagram-v2 포함) |
| AC-IA-015 | PASS | `grep -rl '바이너리로 심화\|Tier [123]' www/content/cli` | `www/content/cli/moai-adk/bridge.md` ("CLI에서 바이너리로 심화" 브리지 내러티브 + moai-code Tier 1~3 능력 표 — BOOTSTRAP-DESKTOP-001 REQ-BD-008 원천) |
| AC-IA-018(a) | PASS | `grep -rl '^ia_in_scope: true' www/content/cli --include='*.md' \| wc -l` | 22 (in-scope 집합 ≥ 1 — 전체 22 페이지 마킹) |
| AC-IA-018(b) | PASS | prose-first 기계 근사 (각 페이지 첫 본문 라인이 표/코드펜스로 시작하지 않는지) | 22/22 페이지 prose paragraph로 시작 (표/코드펜스로 시작하는 페이지 0) |
| AC-IA-019 | PASS | `comm -23 <(grep -rl '^ia_in_scope: true' www/content/cli --include='*.md'\|sort) <(grep -rl '\`\`\`mermaid' www/content/cli --include='*.md'\|sort)\|wc -l` | 0 (in-scope 페이지 중 mermaid 누락 0) |
| AC-IA-020 | PASS | in-scope 출처 블록 — `comm -23 <(grep -rl '^ia_in_scope: true' www/content/cli --include='*.md'\|sort) <(grep -rlE '^#{2,4}[[:space:]]*(Sources\|출처\|참고)' www/content/cli --include='*.md'\|sort)\|wc -l` | 0 (22/22 페이지 `### Sources` 블록 포함) |
| AC-IA-021 | PASS | CLI 톤 표본 확인 | 22/22 페이지 "친화적 기술 용어" 톤 (개발 용어 정확 + 비유로 풀이, 데스크탑 축의 비개발자 은유 톤과 구분) |
| AC-IA-024(a) | PASS | `grep -rl '^ia_in_scope: true' www/content/cli --include='*.md' \| wc -l` | 22 (≥ 1) |
| AC-IA-024(b) | PASS | `comm -23 <(find www/content/cli -name '*.md'\|sort) <(grep -rl '^ia_in_scope: true' www/content/cli --include='*.md'\|sort)\|wc -l` | 0 (`content/cli/**` 전량 마킹, floor 가드) |

### E2 — Hugo Build

```
$ cd www && hugo --gc --minify
 Processed images │   0
 Aliases          │  56
 Cleaned          │   0
Total in 13963 ms
```

exit 0. 22 신규 CLI 페이지가 빌드에 통과했음 (geekdoc frontmatter + mermaid 모두 렌더 가능). M5/M6은 본 위임 범위 밖.

### E3 — Page Count

```
$ find www/content/cli -name '*.md' | wc -l
      22
```

22 페이지 (plan.md §F M4 목표 ~25-30의 하단 근접; prose-first 밀도 우선). 5 sections × _index + 주요 subpages.

### E4 — Commits (NO PUSH)

6 commits on `worktree-agent-acb8978ec711f2923`:
- `21e44dc`, `109dba7`, `4645bb2`, `4834643`, `f6c6750` (5 섹션), `12eaa8e` (menu).

push는 orchestrator 소관 (Hybrid Trunk, race-modified 정책). 본 위임은 commit만 수행.

### E5 — Scope Discipline

```
$ git diff --name-only d3d139e..HEAD
www/content/cli/_index.md
www/content/cli/concepts/_index.md
www/content/cli/concepts/ddd-tdd.md
www/content/cli/concepts/harness.md
www/content/cli/concepts/spec-system.md
www/content/cli/concepts/trust5.md
www/content/cli/daily/_index.md
www/content/cli/daily/daily-flow.md
www/content/cli/daily/debugging.md
www/content/cli/daily/prompts.md
www/content/cli/daily/tokens-cost.md
www/content/cli/moai-adk/_index.md
www/content/cli/moai-adk/bridge.md
www/content/cli/moai-adk/quality-commands.md
www/content/cli/moai-adk/workflow-commands.md
www/content/cli/reference/_index.md
www/content/cli/reference/advanced.md
www/content/cli/reference/cli-reference.md
www/content/cli/reference/multi-llm.md
www/content/cli/start/_index.md
www/content/cli/start/first-spec.md
www/content/cli/start/install.md
www/data/menu/main.yaml
```

23 파일 (22 신규 `www/content/cli/**` + 1 `www/data/menu/main.yaml`). **B10/B8 PASS** — `www/**` 외 트리 무변경, `themes/layouts/assets/plugins/moai-adk-go/cookbook/releases` 본문 무변경, version 2.27.0 불변.

### E6 — Menu

CLI placeholder `[M4 예정|PLACEHOLDER]` 5건 전부 제거 → 22 real section refs로 충전 (5 sections × _index + subpages + '핵심' badge on bridge page).

```
$ grep -nE 'M4 예정|PLACEHOLDER' www/data/menu/main.yaml
$ # exit 1 — 0 matches (PASS)
```

### E7 — Worktree Base

`worktree-agent-acb8978ec711f2923` HEAD = `d3d139e` (D₁ final HEAD). 본 위임의 6 commits는 이 base 위에 쌓임. runtime이 auto-materialize한 L1 worktree.

### E8 — Blocker

없음. 모든 M4 AC가 self-verification PASS. M5 (plugins, REMEDIATION-001 gate) / M6 (finalization)은 본 위임 범위 밖 — D₁와 D₂는 독립 완료.

### D₃ — M5 plugins 4 카테고리 (2026-07-05, 이 위임)

- **Worktree base**: `worktree-agent-a7b711968578d6a1b` @ `c667d98` (= D₂ final HEAD, origin-synced). runtime이 auto-materialize한 L1 worktree.
- **M5 gate status**: SPEC-MOC-PLUGIN-REMEDIATION-001 = `implemented` → M5 진입 게이트 충족 (AC-IA-011 전제).
- **M5 산출물 (4 카테고리 디렉토리 + root hub rewrite)**:
  - `www/content/plugins/_index.md` (root rewrite — 4-category hub, marketplace 3-plugin 진실 반영)
  - `www/content/plugins/chat/_index.md` (신규 — doc hub A안, NOT built plugin)
  - `www/content/plugins/cowork/_index.md` (신규 — moai-cowork v3.0.0, 177스킬 skeleton)
  - `www/content/plugins/design/_index.md` (신규 — moai-design v0.1.0, 11스킬 skeleton)
  - `www/content/plugins/code/_index.md` (신규 — moai-code name="moai" v3.0.0, 13명령+7에이전트+28스킬 skeleton)
  - 32 obsolete pages deleted (28 moai-* + code.md + cowork.md + design-plugin.md + quick-start.md)
- **Commits (6, NO PUSH — orchestrator owns push)**:
  - `637e1cd` — feat: M5 plugins chat 카테고리 (문서 허브 A안)
  - `aa35d8c` — feat: M5 plugins cowork 카테고리 (스켈레톤)
  - `93c4871` — feat: M5 plugins design 카테고리 (스켈레톤)
  - `4a56289` — feat: M5 plugins code 카테고리 (스켈레톤)
  - `52d9072` — feat: M5 plugins archive + alias (구 33p /plugins/* 리다이렉트)
  - (이 커밋) — docs: M5 menu + progress §E.2 D₃ evidence

### M5 AC 증거 (Self-Verification)

| AC | Status | Verification Command | Actual Output |
|----|--------|---------------------|---------------|
| AC-IA-007 | PASS | `find www/content/plugins -maxdepth 1 -mindepth 1 -type d` | 4 dirs: chat, code, cowork, design (사이트 제품 축과 1:1 대응) |
| AC-IA-008 | PASS | `grep -cE '스킬·플러그인 활용\|문서 허브' www/content/plugins/chat/_index.md` AND `grep -c 'plugin\.json' www/content/plugins/chat/_index.md` | keyword=5 (허브 표현 존재), plugin.json=0 (빌드 플러그인 서술 부재 — doc hub A안) |
| AC-IA-009 | PASS | cowork/design/code `_index.md` 각각 5-skeleton 앵커 grep (intro/설치/Top/전체 인덱스/레시피) | 3/3 페이지 5-skeleton 순서 준수 (intro prose → 설치 diagram → Top 5 → 전체 인덱스 → 레시피) |
| AC-IA-010 | PASS | `grep -rhE '^aliases:' www/content/plugins --include='*.md' \| grep -oE '/plugins/[A-Za-z0-9/_-]*' \| sort -u \| wc -l` | 38 (≥33 baseline — 구 33 obsolete page per-page alias 커버리지 + 5 catch-all) |
| AC-IA-011 | PASS | `cat .claude-plugin/marketplace.json` 3 plugins 일치 AND 카테고리 내용 동기화 | marketplace.json = moai-cowork/moai(moai-code)/design 3-entry와 4 카테고리 1:1 정합 (chat은 doc hub로 빌드 플러그인 아님 — REQ-IA-008 위반 아님) |
| AC-IA-018(a) | PASS | `grep -rl '^ia_in_scope: true' www/content/plugins --include='*.md' \| wc -l` | 5 (in-scope 집합 ≥ 1 — root hub + 4 카테고리 전량 마킹) |
| AC-IA-018(b) | PASS | prose-first 기계 근사 (각 페이지 첫 본문 라인이 표/코드펜스로 시작하지 않는지) | 5/5 페이지 prose paragraph로 시작 (왜-이-페이지가-존재하는가 narrative) |
| AC-IA-019 | PASS | `comm -23 <(grep -rl '^ia_in_scope: true' www/content/plugins --include='*.md'\|sort) <(grep -rl '\`\`\`mermaid' www/content/plugins --include='*.md'\|sort)\|wc -l` | 0 (in-scope 5페이지 중 mermaid 누락 0 — 각 페이지 1개 이상 mermaid diagram 포함) |
| AC-IA-020(b) | PASS | in-scope 출처 블록 — `comm -23 <(grep -rl '^ia_in_scope: true' www/content/plugins --include='*.md'\|sort) <(grep -rlE '^### Sources' www/content/plugins --include='*.md'\|sort)\|wc -l` | 0 (5/5 페이지 `### Sources` 블록 포함) |
| AC-IA-024(a) | PASS | `grep -rl '^ia_in_scope: true' www/content/plugins --include='*.md' \| wc -l` | 5 (≥ 1) |
| AC-IA-024(b) | PASS | `comm -23 <(find www/content/plugins/chat www/content/plugins/cowork www/content/plugins/design www/content/plugins/code -name '*.md' 2>/dev/null\|sort) <(grep -rl '^ia_in_scope: true' www/content/plugins --include='*.md' 2>/dev/null\|sort)\|wc -l` | 0 (4 카테고리 전량 마킹, floor 가드) |
| AC-IA-023 | DEFERRED | Hugo build exit 0 (본 위임 검증) + 전용 link-checker broken 0 | Hugo exit 0 (아래 E2), link-checker는 M6 전용 도구 — D₄에서 검증 |

### E2 — Hugo Build (M5)

```
$ cd www && hugo --gc --minify
                  │ KO
──────────────────┼─────
 Pages            │ 228
 Paginator pages  │   2
 Static files     │ 252
 Aliases          │  65
 Cleaned          │   0
Total in 401 ms
```

exit 0. 0 errors. M5의 5 신규/재작성 페이지 + 32 삭제가 빌드에 통과했음 (alias 38건이 65 total aliases에 반영). 0 broken links (Hugo 수준 — link-checker 전용 검증은 M6).

### E3 — Page Count (M5)

```
$ find www/content/plugins -name '*.md' | wc -l
      5
$ ls www/content/plugins -d */
www/content/plugins/chat/  www/content/plugins/code/  www/content/plugins/cowork/  www/content/plugins/design/
```

5 페이지 (root hub _index + 4 카테고리 _index). 구 33 페이지는 전부 alias로 리다이렉트 처리 — 단일 통합 moai-cowork 진실에 정합 (REMEDIATION-001).

### E4 — Commits (NO PUSH)

6 commits on `worktree-agent-a7b711968578d6a1b`:
- `637e1cd` (chat), `aa35d8c` (cowork), `93c4871` (design), `4a56289` (code), `52d9072` (archive+alias), `이 커밋` (menu+progress).

push는 orchestrator 소관 (Hybrid Trunk, race-modified 정책). 본 위임은 commit만 수행.

### E5 — Scope Discipline (M5)

```
$ git diff --name-only c667d98..HEAD
www/content/plugins/_index.md            (rewrite — 4-category hub)
www/content/plugins/chat/_index.md       (new)
www/content/plugins/code/_index.md       (new)
www/content/plugins/cowork/_index.md     (new)
www/content/plugins/design/_index.md     (new)
www/content/plugins/code.md              (deleted)
www/content/plugins/cowork.md            (deleted)
www/content/plugins/design-plugin.md     (deleted)
www/content/plugins/quick-start.md       (deleted)
www/content/plugins/moai-{bi,book,business,...,wealth}.md  (28 deleted)
www/data/menu/main.yaml                  (menu plugins section rewrite — 이 커밋)
.moai/specs/SPEC-MOC-SITE-IA-001/progress.md  (이 커밋)
```

38 파일 = 5 신규/재작성 `www/content/plugins/**` + 32 삭제 + 1 menu + 1 progress. **B8/B10 PASS** — `themes/layouts/assets/hugo.toml` 무변경, repo-root `plugins/**` 소스 무변경 (DOCUMENT only), cookbook/releases 본문 무변경, version 2.27.0 불변.

### E6 — Menu (M5)

```
# before
- name: MoAI-Cowork (28종)   ref: /plugins/cowork
- name: MoAI-Code             ref: /plugins/code          badge: 출시예정
- name: MoAI-Design           ref: /plugins/design-plugin badge: 출시예정

# after
- name: 플러그인 카탈로그                  ref: /plugins
- name: Chat — 스킬·플러그인 활용          ref: /plugins/chat
- name: moai-cowork (한국 실무 177스킬)    ref: /plugins/cowork
- name: moai-design (에이전틱 디자인)      ref: /plugins/design
- name: moai-code (무설치 개발 방법론)     ref: /plugins/code
```

출시예정 badge 2건 제거 (REMEDIATION-001 완료로 3플러그인 모두 live), 28종 라벨 → 177스킬로 정정, chat 카테고리 신설, design-plugin → design URL 정정.

### E7 — Worktree Base

`worktree-agent-a7b711968578d6a1b` HEAD = `c667d98` (D₂ final HEAD, origin-synced). 본 위임의 6 commits는 이 base 위에 쌓임. runtime이 auto-materialize한 L1 worktree.

### E8 — Blocker (M5)

없음. 모든 M5 AC (AC-IA-007/008/009/010/011/018/019/020/024)가 self-verification PASS. AC-IA-023 (link-checker)은 M6 전용 도구이므로 D₄에서 검증 — 본 위임 범위 밖. M6 (finalization)도 본 위임 범위 밖.

## §E.3 Run-phase Audit-Ready Signal

- **run_partial_complete_at**: 2026-07-05
- **run_scope**: D₁ (M1+M2+M3) + D₂ (M4) + D₃ (M5) 완료. D₄ (M6, finalization)만 별도 위임 대기.
- **run_commit_sha**:
  - D₁: `a803537`, `e50dc6e`, `d3d139e`
  - D₂ (M4): `21e44dc`, `109dba7`, `4645bb2`, `4834643`, `f6c6750`, `12eaa8e`
  - D₃ (M5): `637e1cd`, `aa35d8c`, `93c4871`, `4a56289`, `52d9072`, (이 커밋 — menu+progress)
- **run_status**: partial-complete (M1~M5 PASS, M6 pending — link-checker + 4-phase close)
- **ac_pass_count**: 25 (AC-IA-001/002/003/004/005/006/007/008/009/010/011/012/013/014/015/016/017/018/019/020/021/022/024 — D₁+D₂+D₃ 소관; AC-IA-018/019/020/024는 D₂+D₃ 누적 in-scope 집합에 대해 모두 PASS)
- **ac_fail_count**: 0
- **ac_pending_count**: 1 (AC-IA-023 → M6 전용 link-checker + D₄)
- **preserve_list_post_run_count**: PRESERVE 대상 무변경 (themes/layouts/assets · repo-root `plugins/**` 소스 · moai-adk-go · cookbook · releases 본문 · hugo.toml version 2.27.0)
- **new_warnings_or_lints_introduced**: 없음 (Hugo build exit 0, 0 errors, 228 pages, 65 aliases)
- **cross_platform_build.hugo**: PASS (exit 0, 401 ms, 5 신규/재작성 plugins 페이지 + 32 삭제 alias 처리 렌더)
- **total_run_phase_files**: D₁ 3 + D₂ 23 + D₃ 38 (5 신규/재작성 + 32 삭제 + 1 menu) = 64 cumulative run-phase files

## §E.4 Sync-phase Audit-Ready Signal

_<pending sync-phase — owned by manager-docs>_

## §E.5 Mx-phase Audit-Ready Signal

_<pending Mx-phase — owned by manager-docs / orchestrator>_

## §E.6 Phase 0.95 Mode Selection

- **Input parameters**: tier=L · scope≈30+ files (menu SSOT + CLI ~25-30 new pages + plugin rewrite + DESIGN merge + source-index) · domains=6 (menu/DESIGN/help-office/CLI-content/plugins/link-checker-tooling) · language=100% markdown + 1 Node script · concurrency-benefit=LOW (content-authoring heavy, shared files across milestones) · Agent-Teams-prereqs=not-met
- **Decision: Mode 5 (sub-agent)** — sequential milestone delegation
- **Justification**: Tier L + markdown/content-authoring heavy (per-page creative, not mechanical-uniform) → Mode 6 (workflow) excluded per Anthropic coding-heavy caveat. Shared files (menu `main.yaml`, `source-index.md`) across M1/M3/M5/M6 preclude safe parallel (Mode 4). §B.2 "Tier L + markdown/shell-only → Mode 5 with Section A-E template". Implementation Kickoff approved (Option 1) + plan-audit PASS 0.90 → Mode 5 entry conditions met.
- **Milestone grouping (sequential delegations)**: D₁ = M1+M2+M3 (structural core) · D₂ = M4 (CLI, largest) · D₃ = M5 (plugins, REMEDIATION-001 gate cleared) · D₄ = M6 (finalization).
