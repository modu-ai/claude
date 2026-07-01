<!-- source-spec: docs/plugin-family-design/03-moai-design-processing.md §5.1 -->
---
description: 하이브리드 디자인 워크플로우 — Path A(Claude Design import) 또는 Path B(코드 기반 브랜드 디자인) 경로 선택
argument-hint: "[자연어 요청]"
allowed-tools: Skill
---

Route the request into the `/design` hybrid workflow (Path A Claude Design import vs Path B code-based brand design). The orchestrator collects the path choice via AskUserQuestion before entering the pipeline.

Use Skill("moai-workflow-design") with arguments: $ARGUMENTS

(UX prompt pattern advisor available via Skill("cd-prompt-builder").)
