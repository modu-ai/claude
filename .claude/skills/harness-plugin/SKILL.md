---
name: harness-plugin
description: Companion skill for /harness:plugin — generates desktop plugin (cowork/code) core skills from a 3-Layer research pipeline (qmd vault → Claude official docs → web search) with category constraints.
metadata:
  version: "0.1.0"
  category: harness
  status: active
  updated: 2026-07-08
  tags: "harness, plugin, skill-generation, qmd, claude-docs"
---

# harness-plugin — Desktop Plugin Skill Generator

Companion skill for the `/harness:plugin` harness. Turns a natural-language directive into a plugin-scoped core skill via a 6-Phase pipeline with 3-Layer research.

## 6-Phase Pipeline (Pipeline + Producer-Reviewer)

1. **Discovery** (`intent-parser`) — parse natural-language `$ARGUMENTS` → target plugin (cowork/code) + skill topic + intent. Returns structured block (NOT free-form). The orchestrator surfaces ambiguities via AskUserQuestion.
2. **3-Layer Research** (`research-collector`, dynamic-workflow fan-out):
   - Layer 1 qmd vault — `scripts/qmd-search.sh "<keyword>" [TOP_N]`
   - Layer 2 Claude official docs — `code.claude.com/docs`, `docs.claude.com`
   - Layer 3 web search — supplementary
3. **Curation** (`plugin-curator`) — 4-dimension rubric (Relevance / Specificity / Practicality / Reusability, 0–5 each), top-5 selection. Producer-Reviewer pattern: curator is the evaluator.
4. **User Report & Selection** — orchestrator surfaces top-5 via AskUserQuestion.
5. **Build** (`skill-builder`, opus/high) — generate the plugin-scoped skill under the category constraints.
6. **Test + Review + Final Report**.

## Category Constraints (HARD — skill-builder enforces)

| Target plugin | Allowed categories | Forbidden categories |
|---------------|-------------------|---------------------|
| cowork / designer / pm (code-외) | `skills/` | `commands/`, `agents/`, `hooks/`, `output-styles/`, `rules/`, `mcp-servers/` |
| code | `commands/`, `skills/`, `agents/` | `hooks/`, `output-styles/`, `rules/`, `mcp-servers/` |

## qmd Layer (Layer 1)

- Wrapper: `scripts/qmd-search.sh "<query>" [TOP_N]` — qmd hybrid (BM25 + semantic + LLM rerank), automatic ripgrep fallback when qmd unavailable or vectors < `VAULT_QMD_MIN_VECTORS` (default 1000).
- Env vars: `VAULT_QMD_COLLECTION` (default `moai-vault`), `VAULT_SEARCH_TOP` (default 10), `MOAI_OBSIDIAN_VAULT`.
- Auto-sync: `scripts/sync.sh --quiet` runs before search (incremental qmd update + embed).

## References

- Manifest: `.claude/commands/harness/plugin/manifest.json`
- Runner: `.claude/workflows/harness-plugin-run.js`
- Entry command: `.claude/commands/harness/plugin.md`
