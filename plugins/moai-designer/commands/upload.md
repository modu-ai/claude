---
description: 디자인 시스템 자산을 Claude Design에 업로드 — 자동(DesignSync MCP) 우선 + 수동 폴백
argument-hint: "[DESIGN.md / 자산 폴더 경로]"
allowed-tools: Skill
---
<!-- source-spec: docs/plugin-family-design/03-moai-design-processing.md §5.1 -->

Upload design system assets to Claude Design (auto-first with manual fallback).

Use Skill("design-sync-upload") with arguments: $ARGUMENTS

Auto path uses the DesignSync MCP (`write_files` / `register_assets` / `finalize_plan`) and requires `/design-login`. When unauthenticated or the MCP is unavailable, it falls back to emitting `UPLOAD-GUIDE.md` + a staged asset folder for manual upload.
