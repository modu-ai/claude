#!/bin/bash
# moai-code 무설치 자기완결 훅 — session-start
# parity-source: internal/template/templates/.claude/hooks/moai/handle-session-start.sh.tmpl @ b1ff846c4
#
# 정본 `moai hook session-start` 래퍼의 무설치 대체. moai 바이너리 셸아웃을 제거한 무설치 패턴.
# O클래스(관측): stdin 비차단 통과. 실질 품질 게이트는 KEEP 훅
# (sync-phase-quality-gate / status-transition-ownership / team-ac-verify)이
# hooks.json에 병렬 등록되어 담당한다(04 §5.1·§5.3).
#
# REQ-BD-009 / AC-BD-005a: moai 바이너리 탐지 분기 — 존재 시 1줄 승격 안내(promotion notice).
# REQ-BD-010 / AC-BD-005b: 바이너리 부재 시 무음 fail-open (기존 무설치 자기완결 훅 패턴 재사용,
#   사용자 흐름 차단·에러 노출 금지).

# stdin을 비차단으로 소비(정본 래퍼 호환 — session-start 이벤트 JSON 드레인)
cat >/dev/null 2>&1 || true

# 바이너리 탐지 분기 — 승격 안내 / 무음 fail-open (AC-BD-005a NET-NEW)
if command -v moai >/dev/null 2>&1; then
  # 바이너리 존재 — Tier 3 승격 1줄 안내. stderr로 출력해 stdout 워크플로우 오염 방지.
  printf '[moai-code] moai 바이너리 탐지 — Tier 3 승격(네이티브 훅 강제·LSP 진단 게이트·cg/glm 비용 모드) 가능. `moai doctor`로 드리프트 확인.\n' >&2 || true
fi

# 무음 fail-open (AC-BD-005b PRESERVE — 사용자 흐름 차단 금지)
exit 0
