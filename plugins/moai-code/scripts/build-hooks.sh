#!/usr/bin/env bash
# build-hooks.sh — moai-code 무설치 훅 자기완결화 (P2)
#
# 정본의 훅 시스템을 moai 바이너리 셸아웃 없이 재구현한다.
# 설계 근거: docs/plugin-family-design/04-moai-code-processing.md §4·§5
#
# 전략:
#   - KEEP 4개(.sh, moai 무의존): 정본 그대로 복사 → 실질 게이트
#   - handle-* 래퍼(moai hook 셸아웃): 자기완결 no-op으로 대체(O클래스, §5.3)
#   - hooks.json: settings.json.tmpl에서 Platform=else + HookOptIn=false 렌더 후
#                 경로를 ${CLAUDE_PLUGIN_ROOT}로 치환
#   - DROP: harness-observe 4 + iggda-phase-driver (HookOptIn 블록 → 미등록)

set -euo pipefail

SRC="${MOAI_TEMPLATE_SRC:-/Users/goos/moai/moai-adk-go/internal/template/templates}"
DEST="${MOAI_CODE_DEST:-$(cd "$(dirname "$0")/.." && pwd)}"
HOOKS_SRC="$SRC/.claude/hooks/moai"
HOOKS_DEST="$DEST/hooks/moai"
SETTINGS="$SRC/.claude/settings.json.tmpl"

if git -C "$SRC" rev-parse HEAD >/dev/null 2>&1; then PIN=$(git -C "$SRC" rev-parse --short HEAD); else PIN="unknown"; fi
echo "▸ P2 훅 자기완결화 — parity-source @ $PIN"

mkdir -p "$HOOKS_DEST"
rm -f "$HOOKS_DEST"/*.sh 2>/dev/null || true

# ============================================================
# 1. hooks.json 생성 (Platform=else, HookOptIn=false, 경로 치환)
# ============================================================
echo "▸ [1/3] hooks.json 생성"
python3 - "$SETTINGS" "$DEST/hooks/hooks.json" <<'PY'
import re, json, sys
settings, out = sys.argv[1], sys.argv[2]
raw = open(settings).read()
# Platform windows/else → else 분기 채택
raw = re.sub(r'\{\{-?\s*if eq \.Platform "windows"\}\}.*?\{\{-?\s*else\}\}(.*?)\{\{-?\s*end\}\}', r'\1', raw, flags=re.DOTALL)
# HookOptIn.Enabled 블록 제거 (harness-observe/iggda 미등록)
raw = re.sub(r'\{\{\s*if \.HookOptIn\.Enabled\s*\}\}.*?\{\{\s*end\s*\}\}', '', raw, flags=re.DOTALL)
# 잔여 Go 템플릿 토큰 제거
raw = re.sub(r'\{\{-?.*?\}\}', '', raw)
data = json.loads(raw)
hooks = data.get('hooks', {})
s = json.dumps({'hooks': hooks}, indent=2, ensure_ascii=False)
# 무설치 경로 치환: 프로젝트 훅 경로 → 플러그인 번들 경로
s = s.replace('$CLAUDE_PROJECT_DIR/.claude/hooks/moai/', '${CLAUDE_PLUGIN_ROOT}/hooks/moai/')
open(out, 'w').write(s + '\n')
# 등록된 스크립트 목록 출력
scripts = sorted(set(re.findall(r'hooks/moai/([a-z0-9-]+\.sh)', s)))
print('  등록 훅 스크립트: ' + str(len(scripts)))
for x in scripts: print('    ' + x)
PY

# ============================================================
# 2. KEEP 4개 (.sh, moai 무의존) 정본 복사
#    실측 검증: moai 참조는 주석/.moai 경로 문자열뿐, exec moai 없음 (04 §5.1)
# ============================================================
echo "▸ [2/3] KEEP 훅 복사 (실질 게이트)"
for k in status-transition-ownership sync-phase-quality-gate team-ac-verify iggda-audit-preservation-guard; do
  if [ -f "$HOOKS_SRC/$k.sh" ]; then
    cp "$HOOKS_SRC/$k.sh" "$HOOKS_DEST/$k.sh"
    echo "    KEEP: $k.sh"
  fi
done

# ============================================================
# 3. handle-* 래퍼 자기완결화 (hooks.json이 참조하는 것만)
#    O클래스(관측): stdin 비차단 통과. moai 셸아웃 제거.
#    실질 게이트는 KEEP 훅(2단계)이 병렬 등록되어 담당.
# ============================================================
echo "▸ [3/3] handle-* 래퍼 자기완결화 (no-op, moai 셸아웃 제거)"
mk_noop() {
  local name="$1" event="$2"
  cat > "$HOOKS_DEST/$name" <<EOF
#!/bin/bash
# moai-code 무설치 자기완결 훅 — $event
# parity-source: internal/template/templates/.claude/hooks/moai/$name.tmpl @ $PIN
#
# 정본 \`moai hook $event\` 래퍼의 무설치 대체. moai 바이너리 셸아웃 제거.
# O클래스(관측): stdin 비차단 통과. 실질 품질 게이트는 KEEP 훅
# (sync-phase-quality-gate / status-transition-ownership / team-ac-verify)이
# hooks.json에 병렬 등록되어 담당한다(04 §5.1·§5.3).
cat >/dev/null 2>&1 || true
exit 0
EOF
}
noop_count=0
# hooks.json이 참조하는 handle-*.sh 중 KEEP 아닌 것을 no-op 생성
for ref in $(grep -oE 'hooks/moai/handle-[a-z0-9-]+\.sh' "$DEST/hooks/hooks.json" | sed 's|.*/||' | sort -u); do
  event=$(echo "$ref" | sed 's/^handle-//; s/\.sh$//')
  mk_noop "$ref" "$event"
  noop_count=$((noop_count+1))
done
echo "    자기완결 no-op 래퍼: $noop_count"

chmod +x "$HOOKS_DEST"/*.sh 2>/dev/null || true

# ============================================================
# 검증
# ============================================================
echo "▸ 검증"
# 실제 셸아웃 패턴만 검사 (exec moai / command -v moai). 주석의 'moai hook' 언급은
# 추적성 주석이므로 제외 — grep 'moai hook'은 false positive (verification-claim-integrity)
shellout=$( { grep -rn 'exec moai\|command -v moai' "$HOOKS_DEST"/ 2>/dev/null || true; } | wc -l | tr -d ' ')
echo "    훅 트리 실제 moai 셸아웃 잔존: $shellout (기대 0)"
total=$(ls "$HOOKS_DEST"/*.sh 2>/dev/null | wc -l | tr -d ' ')
echo "    총 훅 스크립트: $total"
echo "✓ P2 훅 자기완결화 완료"
