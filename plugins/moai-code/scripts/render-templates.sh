#!/usr/bin/env bash
# render-templates.sh — moai-code 무설치 플러그인 빌드 파이프라인 (P1 범위)
#
# 정본(parity-source) 템플릿 `internal/template/templates/.claude/`를 읽어
# moai-code 플러그인 트리로 렌더/복사한다. moai Go 바이너리 무설치.
#
# 설계 근거: docs/plugin-family-design/04-moai-code-processing.md §3.2
# P1 범위: 명령 정적 렌더(ko) + 스킬/에이전트/규칙/스타일 복사 + parity-source 핀
# P2 범위(별도): 훅 자기완결화, hooks.json, 셸아웃 제거 → 본 스크립트에 미포함
#
# 결정론 요구: wall-clock/난수 미사용. 타임스탬프성 값은 /moai project 부트스트랩이 채운다.

set -euo pipefail

# ---- 경로 ----
SRC="${MOAI_TEMPLATE_SRC:-/Users/goos/moai/moai-adk-go/internal/template/templates}"
DEST="${MOAI_CODE_DEST:-$(cd "$(dirname "$0")/.." && pwd)}"
SRC_CLAUDE="$SRC/.claude"

# ---- parity-source 커밋 핀 ----
if git -C "$SRC" rev-parse HEAD >/dev/null 2>&1; then
  PIN=$(git -C "$SRC" rev-parse --short HEAD)
elif git -C "$SRC/../../.." rev-parse HEAD >/dev/null 2>&1; then
  PIN=$(git -C "$SRC/../../.." rev-parse --short HEAD)
else
  PIN="unknown"
fi
echo "▸ parity-source: $SRC @ $PIN"

# ---- D7: 디자인/brain 명령 제외 ----
EXCLUDE_CMDS="design brain"

# ============================================================
# 1. 명령 정적 렌더 (12 .md.tmpl → .md, ko 기본)
#    D8(2026-07-01): 플러그인 명령은 flat commands/*.md → /moai:<name>.
#    plugin.json name="moai"가 콜론 네임스페이스를 제공하므로 정본의
#    commands/moai/ 서브디렉토리를 flatten한다. (서브디렉토리는 플러그인에서
#    typed 이름에 반영되지 않음 — 공식 문서 검증, docs 04 §명령 네임스페이싱)
#    Go text/template의 {{if eq .ConversationLanguage "ko"}}...{{else...}}{{end}}
#    조건문에서 ko 분기만 추출한다. 명령 본문은 변수 없는 한 줄.
# ============================================================
echo "▸ [1/5] 명령 렌더 (ko, flat → /moai:<name>)"
render_go_cond() {
  # stdin의 {{if eq .ConversationLanguage "ko"}}KO{{else if ...}}...{{end}} → KO
  perl -0pe 's/\{\{if eq \.ConversationLanguage "ko"\}\}(.*?)\{\{else.*?\{\{end\}\}/$1/gs' \
  | perl -0pe 's/\{\{if eq \.ConversationLanguage "ko"\}\}(.*?)\{\{end\}\}/$1/gs'
}
mkdir -p "$DEST/commands"
rm -rf "$DEST/commands/moai"   # D8: 이전 서브디렉토리 레이아웃 정리
cmd_count=0
for f in "$SRC_CLAUDE"/commands/moai/*.md.tmpl; do
  [ -e "$f" ] || continue
  base=$(basename "$f" .md.tmpl)
  case " $EXCLUDE_CMDS " in *" $base "*) echo "    skip(D7): $base"; continue;; esac
  out="$DEST/commands/$base.md"
  {
    echo "<!-- parity-source: internal/template/templates/.claude/commands/moai/$base.md.tmpl @ $PIN -->"
    render_go_cond < "$f"
  } > "$out"
  cmd_count=$((cmd_count+1))
done
# 정적 .md 명령 복사 (harness.md 등; design/brain 제외)
for f in "$SRC_CLAUDE"/commands/moai/*.md; do
  [ -e "$f" ] || continue
  base=$(basename "$f" .md)
  case " $EXCLUDE_CMDS " in *" $base "*) echo "    skip(D7): $base"; continue;; esac
  cp "$f" "$DEST/commands/$base.md"
  cmd_count=$((cmd_count+1))
done
echo "    렌더/복사된 명령: $cmd_count (flat → /moai:<name>)"

# ============================================================
# 2. 에이전트 복사 (7 파일)
#    hooks: 프론트매터의 셸아웃 치환은 P2 범위 — 여기서는 원본 복사
# ============================================================
echo "▸ [2/5] 에이전트 복사"
cp "$SRC_CLAUDE"/agents/moai/*.md "$DEST/agents/moai/"
agent_count=$(ls "$DEST"/agents/moai/*.md | wc -l | tr -d ' ')
echo "    에이전트: $agent_count"

# ============================================================
# 3. 스킬 복사 (28 디렉토리; 순수 지식)
#    라우터 셸아웃 문구 치환은 P1 후속(4단계)에서 수행
# ============================================================
echo "▸ [3/5] 스킬 복사"
for d in "$SRC_CLAUDE"/skills/*/; do
  name=$(basename "$d")
  rm -rf "$DEST/skills/$name"
  cp -R "$d" "$DEST/skills/$name"
done
skill_count=$(find "$DEST"/skills -maxdepth 1 -mindepth 1 -type d | wc -l | tr -d ' ')
echo "    스킬 디렉토리: $skill_count"

# ============================================================
# 4. 규칙 + 출력 스타일 복사 (순수 지식/스타일)
# ============================================================
echo "▸ [4/5] 규칙 + 출력 스타일 복사"
rm -rf "$DEST/rules/moai"
cp -R "$SRC_CLAUDE"/rules/moai "$DEST/rules/moai"
cp "$SRC_CLAUDE"/output-styles/moai/*.md "$DEST/output-styles/" 2>/dev/null || true
rules_count=$(find "$DEST"/rules -type f | wc -l | tr -d ' ')
echo "    규칙 파일: $rules_count"

# ============================================================
# 5. P1 정합성 검증
# ============================================================
echo "▸ [5/5] 정합성 검증"
# 5a. 명령에 미치환 Go 템플릿 토큰 0 (parity-source 주석 제외)
leftover=$( { grep -rn '{{' "$DEST/commands/" 2>/dev/null || true; } | { grep -v 'parity-source' || true; } | wc -l | tr -d ' ')
echo "    명령 잔존 {{ }} 토큰: $leftover (기대 0)"
# 5b. design/brain/coverage/e2e 명령 미포함 (D7 + 은퇴)
d7=$( { ls "$DEST"/commands/ 2>/dev/null || true; } | { grep -cE '^(design|brain|coverage|e2e)\.md$' || true; } )
echo "    design/brain/coverage/e2e 명령: $d7 (기대 0)"
# 5c. flat 구조 확인 (commands/moai/ 서브디렉토리 부재)
flat=$( [ -d "$DEST/commands/moai" ] && echo "서브디렉토리 잔존!" || echo "flat OK" )
echo "    명령 구조: $flat (/moai:<name> 형태)"

echo "✓ P1 렌더 완료 — commands:$cmd_count agents:$agent_count skills:$skill_count rules:$rules_count"
