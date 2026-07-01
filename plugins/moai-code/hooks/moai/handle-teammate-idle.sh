#!/bin/bash
# moai-code 무설치 자기완결 훅 — teammate-idle
# parity-source: internal/template/templates/.claude/hooks/moai/handle-teammate-idle.sh.tmpl @ b1ff846c4
#
# 정본 `moai hook teammate-idle` 래퍼의 무설치 대체. moai 바이너리 셸아웃 제거.
# O클래스(관측): stdin 비차단 통과. 실질 품질 게이트는 KEEP 훅
# (sync-phase-quality-gate / status-transition-ownership / team-ac-verify)이
# hooks.json에 병렬 등록되어 담당한다(04 §5.1·§5.3).
cat >/dev/null 2>&1 || true
exit 0
