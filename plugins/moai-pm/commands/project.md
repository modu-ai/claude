---
description: 프로젝트 폴더 초기화 — --cowork(기본)는 goose 스킬, --code는 개발 중(추후 moai 스킬 라우팅 예정)
argument-hint: "[--cowork|--code] <자연어 지시>"
allowed-tools: Skill
---
<!-- moai-pm /project v1.1.0 · 모드 라우터 (cowork → goose, code → 개발 중) -->

Parse $ARGUMENTS for a mode flag:

- `--code` present → **개발 중 (미배포)**: DO NOT invoke any skill. Respond in the user's language:
  "`--code` 모드(개발 프로젝트 초기화, `moai init` 동등 효과)는 현재 개발 중입니다. 코더 플러그인 배포와 함께 지원될 예정입니다. 지금은 `/project --cowork <지시>` 또는 `/moai-pm:moai`(가이던스 전용)를 사용해 주세요."
  <!-- TODO(배포 시): --code → Skill("moai-pm:moai") with arguments: project <나머지 인자> 로 라우팅 -->

- `--cowork` present, or NO mode flag (default) → Use Skill("moai-pm:goose") with arguments: --project <나머지 인자 (모드 플래그 제거 후)>
