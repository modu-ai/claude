---
description: >
  Generates project documentation from codebase analysis or user input.
  Creates product.md, structure.md, and tech.md in .moai/project/ directory,
  plus architecture maps in .moai/project/codemaps/ directory.
  Supports new and existing project types with LSP server detection.
  Use when initializing projects or generating project documentation.
user-invocable: false
metadata:
  version: "2.5.0"
  category: "workflow"
  status: "active"
  updated: "2026-02-21"
  tags: "project, documentation, initialization, codebase-analysis, setup"

# MoAI Extension: Progressive Disclosure
progressive_disclosure:
  enabled: true
  level1_tokens: 100
  level2_tokens: 5000

# MoAI Extension: Triggers
triggers:
  keywords: ["project", "init", "documentation", "setup", "initialize"]
  agents: ["manager-docs", "Explore"]
  phases: ["project"]
---

<!-- TRACE PROBE: workflow-split baseline trace mechanism -->
<!-- Activated by MOAI_TRACE_PHASES=1 environment variable -->
<!-- Emits one line per Phase entry/exit to stderr in format: [trace] /moai project Phase <N> <enter|exit> -->

# Workflow: project - Project Documentation Generation

Purpose: Generate project documentation through smart questions and codebase analysis. Creates product.md, structure.md, and tech.md in .moai/project/ directory, plus architecture documentation in .moai/project/codemaps/ directory.

This workflow is also triggered automatically when project documentation does not exist and the user requests other workflows (plan, run, sync, etc.). See SKILL.md Step 2.5 for the auto-detection mechanism.

---

## Phase Routing Table

| Phase | Sub-skill | Description |
|---|---|---|
| Phase 0.0: No-Install Bootstrap | (this skill §무설치 부트스트랩) | Generate minimal `.moai/config/sections/*` + repo-committed `.claude/settings.json` (no `moai` binary). Runs first when config is absent/incomplete |
| Mode flag / Scope boundary | `project/mode-detection.md` | --mode compatibility, NO SPEC Generation rule |
| Phase 0: Project Type Detection | `project/mode-detection.md` | Auto-detect existing vs. new project |
| Phase 0.3: Deep Interview (New) | `project/mode-detection.md` | 3-round Vision/Technology/Scope interview |
| Phase 1: Codebase Analysis | `project/codebase-analysis.md` | Explore subagent analysis (existing projects) |
| Phase 1.5: Deep Interview (Existing) | `project/codebase-analysis.md` | 3-round Ownership/Constraints/Priority interview |
| Phase 2: User Confirmation | `project/codebase-analysis.md` | Present analysis summary, get proceed/cancel |
| Phase 3: Documentation Generation | `project/doc-generation.md` | manager-docs for product.md/structure.md/tech.md |
| Phase 3.1: Independent Audit | `project/doc-generation.md` | plan-auditor conditional audit + retry loop |
| Phase 3.3: Codemaps Generation | `project/doc-generation.md` | Explore + manager-docs for codemaps/ |
| Phase 3.5: Dev Environment Check | `project/doc-generation.md` | LSP server detection + optional install |
| Phase 3.7: Dev Methodology Config | `project/doc-generation.md` | Auto-set development_mode in quality.yaml |
| Phase 4.1a: DB Detection | `project/doc-generation.md` | Grep/Glob DB keyword detection, db-detection.json |
| Phase 4: Completion | `project/doc-generation.md` | Summary report + 3-branch next-steps AskUserQuestion |
| Phase 5: Socratic Interview | `project/meta-harness.md` | 16Q/4-round harness interview (in-memory buffer) |
| Phase 6: meta-harness Invocation | `project/meta-harness.md` | Skill("moai-meta-harness") + FROZEN guard |

---

## Invocation Flow

```
/moai project
  ├─ [no-install] Phase 0.0 Bootstrap (§무설치 부트스트랩)
  │    └─ generate .moai/config/sections/* + repo .claude/settings.json if absent (idempotent)
  └─ Mode Detection (mode-detection.md)
       ├─ New Project → Phase 0.3 interview → Phase 3 (skip Phase 1/2)
       └─ Existing Project → Phase 1 analysis
                              └─ codebase-analysis.md
                                   ├─ Phase 1.5: 3-Round interview
                                   └─ Phase 2: User Confirmation
                                        └─ doc-generation.md
                                             ├─ Phase 3: Doc generation
                                             ├─ Phase 3.1: Audit (conditional)
                                             ├─ Phase 3.3: Codemaps
                                             ├─ Phase 3.5: LSP check
                                             ├─ Phase 3.7: Dev mode config
                                             ├─ Phase 4.1a: DB detection
                                             └─ Phase 4: Completion
                                                  └─ [optional] Phase 5+6
                                                       └─ meta-harness.md
                                                            ├─ Phase 5: Socratic (4 rounds)
                                                            └─ Phase 6: meta-harness call
```

---

## 무설치 부트스트랩 (No-Install Bootstrap)

> parity-source: `docs/plugin-family-design/04-moai-code-processing.md` §8 — no-install `/moai project` bootstrap. moai-code has no `moai` Go binary, so the config generation `moai init` normally performs is documented here as orchestrator behavior.

Purpose: moai-code is a **no-`moai`-binary plugin** (완전 패리티 무설치, D4). In the binary edition, `moai init` renders `.moai/config/sections/*.yaml` from the go:embed template set. Without the binary, `/moai project` MUST bootstrap the minimal project config itself. Here "bootstrap" means **documented orchestrator behavior** — Read/Write of config files the model performs — **NOT** a binary call. The generation templates are internalized from the parity-source `internal/template/templates/.moai/config/sections/*.tmpl` (04 §3.1).

[HARD] When `/moai project` runs and `.moai/config/sections/` is absent or incomplete, execute this phase FIRST — before Phase 0 (Project Type Detection). This phase is **idempotent**: never overwrite a config section that already exists (respect prior user edits); generate only the missing files.

### Step 0.0.1: Generate minimal config sections

Write the following minimal sections into the user's repo under `.moai/config/sections/`. Values come from the Phase 0.3 interview (new project) or sensible defaults; the plugin resolves the template variables directly (no binary renderer).

| File | Minimal fields | Default / source |
|------|----------------|------------------|
| `language.yaml` | conversation_language, conversation_language_name, agent_prompt_language, git_commit_messages, code_comments, documentation, error_messages | conversation_language default `en` (or interview) |
| `project.yaml` | name, mode, created_at, template_version | name from interview; created_at stamped at write time (runtime, not build) |
| `git-strategy.yaml` | git_provider, git_mode, github_username | provider `github`, mode `hybrid-trunk` default |
| `quality.yaml` | development_mode (ddd/tdd), enforce_quality, test_coverage_target | development_mode auto-set later by Phase 3.7; coverage target 85 default |
| `workflow.yaml` | team.enabled | `false` (team mode is opt-in) |
| `user.yaml` | name, **audience** | name empty default; audience per Step 0.0.2 |

> These are internalized templates (04 §3.1): the Go template variables (`.ConversationLanguage`, `.ProjectName`, …) are resolved here at bootstrap time from interview answers / defaults — never by a binary.

### Step 0.0.2: audience field (D3 — vocabulary invariant, explanation depth only)

- Add an `audience: beginner | developer` field to `.moai/config/sections/user.yaml`. **Default: `developer`.**
- Collect it via **AskUserQuestion on the first `/moai project`** (orchestrator-run; first / recommended option = `developer`).
- [HARD] Per **D3**, audience adjusts **ONLY the explanation depth** in the router skill (`skills/moai/SKILL.md`). The `plan` / `run` / `sync` / `SPEC` / `@MX` vocabulary, the workflow, and the quality gates are **IDENTICAL for all audiences** — there is no beginner-only relaxation of gates and no renaming of commands.

Example AskUserQuestion (orchestrator-run — subagents MUST NOT prompt the user):

- `developer (권장)`: 툴체인 상세·명령 요약 위주의 간결한 안내.
- `beginner`: 각 단계의 배경과 다음 액션을 평문으로 더 자세히 설명 (어휘·워크플로우·게이트는 developer와 동일).

### Step 0.0.3: Commit `.claude/settings.json` to the user's repo

[HARD] Write `.claude/settings.json` into the user's repo (repo-committed, not user-scope) containing:

- **hook registration** — the plugin's `hooks/hooks.json` event map (self-contained shell hooks; no `moai` shellout).
- **non-hook keys** — `permissions`, `env` (and other settings.json non-hook keys) carried from the parity-source `settings.json.tmpl` non-hook part.

Rationale (02 §8.4): a user-scope `+` marketplace install does **NOT** reach cloud/web sessions. Only a **repo-committed `.claude/settings.json`** loads at session start on cloud/web. Committing the hook registration + permissions/env to the repo is what makes the no-install gates reach cloud/web surfaces. The committed hooks depend only on cloud-resident tools (`git`, `jq`, `yq`, `ripgrep`) and never shell out to the removed `moai` binary (guaranteed by the §4/§5 self-contained hooks).

### Step 0.0.4: product.md / structure.md / tech.md via interview

`product.md`, `structure.md`, and `tech.md` are produced by the **Phase 3 documentation-generation** path (`project/doc-generation.md`) from the Phase 0.3 interview (`interview.md`) or codebase analysis — no binary involved. Phase 0.0 only guarantees the config foundation exists before that runs.

### CLAUDE.md is NOT copied

The plugin does **not** copy CLAUDE.md into the user's repo — plugin load already provides the orchestration context (04 §8). Bootstrap writes only the minimal config above plus the repo-committed `.claude/settings.json`.

---

## Detection Keywords Reference

Full DB engine keywords, dependency manifest files (16 languages), and ORM/ODM lists used by Phase 4.1a are defined in `project/doc-generation.md` §Detection Keywords Reference section.

For convenience, the DB engine categories are: Relational/SQL (PostgreSQL, MySQL, MariaDB, SQLite, Oracle, SQL Server, CockroachDB, Supabase, Neon, Planetscale), NoSQL Document (MongoDB, Firestore, Firebase, Couchbase), NoSQL Key-Value (Redis, DynamoDB, Cassandra, ScyllaDB, Riak), Search/Analytics (Elasticsearch, ClickHouse, Snowflake, InfluxDB).

---

Version: 2.5.0
Last Updated: 2026-02-21
SPEC: SPEC-PROJECT-DB-HINT-001, the project-harness generation policy, the workflow-split policy
