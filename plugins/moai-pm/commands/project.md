---
description: 프로젝트 폴더 초기화 — --cowork(기본)는 Cowork 셋업, --code는 개발 중(추후 개발-프로젝트 초기화)
argument-hint: "[--cowork|--code] <자연어 지시>"
allowed-tools: Skill
---
<!-- moai-pm /project v1.2.0 · 단일 진입점 (구 goose·moai 스킬 병합 → skills/project) -->

Use Skill("moai-pm:project") with arguments: $ARGUMENTS

Mode handling is defined inside the skill (§모드 / §Code Mode): `--cowork` or no flag → cowork setup flow; `--code` → "개발 중" guidance only (no generation).
