---
description: Build desktop plugin core skills (cowork/code) via 6-Phase pipeline with 3-Layer research (qmd vault then Claude docs then web)
argument-hint: "[자연어 지시: 타깃 플러그인 + 스킬 주제]"
allowed-tools: Skill
---

# /harness:builder

Dispatches to the `builder` harness. Reads `.claude/commands/harness/builder/manifest.json` (SSOT) and runs the 7-Phase pipeline (Pipeline + Producer-Reviewer patterns) with 5 specialists.

`$ARGUMENTS` is a **natural-language directive** (NOT positional `<plugin> <topic>`). The `intent-parser` specialist extracts target plugin (cowork / code) + skill topic + intent.

## 7-Phase Pipeline

1. **Discovery** (`intent-parser`) — natural-language → plugin + topic + intent
2. **3-Layer Research** (`research-collector`) — Layer 1 qmd vault (priority) → Layer 2 Claude official docs → Layer 3 web search
3. **Curation** (`plugin-curator`) — 4-dimension rubric (Relevance/Specificity/Practicality/Reusability), top-5
4. **User Selection** — orchestrator AskUserQuestion
5. **Build** (`skill-builder`) — plugin skill under category constraints
6. **Audit** (`auditor`) — Claude 공식 문서 기준 감사 (skill-authoring 스키마·카테고리 제약·정합성·중복), PASS or violations
7. **Final Report** — audit verdict 포함

## Category Constraints (skill-builder enforces)

- **code-외 스킬** (cowork / designer / pm): `skills/` category ONLY
- **code 스킬**: `commands/` + `skills/` + `agents/` categories ONLY

## References

- Manifest (SSOT): `.claude/commands/harness/builder/manifest.json`
- Runner: `.claude/workflows/harness-builder-run.js`
- Companion skill: `.claude/skills/harness-builder/SKILL.md`
- Specialists: `.claude/agents/harness/harness-builder-*-specialist.md`
