#!/usr/bin/env bash
# build-moai-design.sh — moai-design 플러그인 조립(assembly) 파이프라인 (COPY 레이어)
#
# 세 출처를 하나의 플러그인 트리로 이식하는 결정론적 COPY 스크립트.
# 설계 근거: docs/plugin-family-design/03-moai-design-processing.md §4 (소스→플러그인 파일 맵)
#
# 출처(3):
#   1. 신세대 디자인 스킬 5종 — claude.mo.ai.kr/.claude/skills/
#   2. 구세대 cd-* 스킬 6종 + 75-브랜드 라이브러리 — MoAI-Cowork-Plugins/moai-design/skills/
#   3. 디자인 헌법 + design.yaml — moai-adk-go 템플릿 정본(FROZEN)
#   + 축소 에이전트 카탈로그 3종 — moai-code 플러그인(이미 plugin-adapted)
#
# 범위(SCOPE): 본 스크립트는 COPY 레이어만 담당한다(raw 이식).
#   SKILL.md frontmatter v0.1.0 정규화(§4.5), plugin.json(§7.1), commands/*.md(§5),
#   README.md(§7.3), slop 사전 ABSORB(§3.3), cd-handoff-reader §5.4 재설계는
#   저작(authored) 산출물로서 Edit/Write로 이 COPY 위에 적용된다(빌드 절차 문서 참조).
#
# 결정론 요구: wall-clock/난수 미사용. 재실행 시 동일 결과(idempotent).
# 저장소 전용 아티팩트 — 배포 번들에 포함되지 않음(not shipped).

set -euo pipefail

# ---- 경로 (parity-source) ----
NEWGEN_SRC="${MOAI_DESIGN_NEWGEN_SRC:-/Users/goos/moai/claude.mo.ai.kr/.claude/skills}"
OLDGEN_SRC="${MOAI_DESIGN_OLDGEN_SRC:-/Users/goos/MoAI/MoAI-Cowork-Plugins/moai-design/skills}"
FROZEN_SRC="${MOAI_DESIGN_FROZEN_SRC:-/Users/goos/moai/moai-adk-go/internal/template/templates}"
AGENT_SRC="${MOAI_DESIGN_AGENT_SRC:-/Users/goos/moai/claude.mo.ai.kr/plugins/moai-code/agents/moai}"
DEST="${MOAI_DESIGN_DEST:-$(cd "$(dirname "$0")/.." && pwd)}"

echo "▸ parity-source(신세대): $NEWGEN_SRC"
echo "▸ parity-source(구세대): $OLDGEN_SRC"
echo "▸ parity-source(FROZEN): $FROZEN_SRC"
echo "▸ parity-source(에이전트): $AGENT_SRC"
echo "▸ dest: $DEST"

# ============================================================
# 1. 디렉토리 골격
# ============================================================
echo "▸ [1/6] 디렉토리 골격"
mkdir -p "$DEST/.claude-plugin" "$DEST/commands" "$DEST/agents" \
         "$DEST/skills" "$DEST/rules/moai/design" "$DEST/config" "$DEST/scripts"

# ============================================================
# 2. 신세대 스킬 5종 (references 하위 트리 포함)
#    parity-source: claude.mo.ai.kr/.claude/skills/<name>/
# ============================================================
echo "▸ [2/6] 신세대 스킬 5종 이식"
NEWGEN="moai-domain-brand-design moai-domain-copywriting moai-workflow-design moai-workflow-gan-loop moai-domain-design-handoff"
for s in $NEWGEN; do
  rm -rf "$DEST/skills/$s"
  cp -R "$NEWGEN_SRC/$s" "$DEST/skills/$s"
  echo "    COPY: $s"
done

# ============================================================
# 3. 구세대 cd-* 스킬 5종 + 라이브러리 1종
#    parity-source: MoAI-Cowork-Plugins/moai-design/skills/<name>/
#    design-system-library는 트리 전체 이식하되 중첩 moai-content/ 제외(§6.5)
# ============================================================
echo "▸ [3/6] 구세대 스킬 6종 이식"
OLDGEN="cd-brief cd-system-prep cd-prompt-builder cd-handoff-reader cd-slop-check design-system-library"
for s in $OLDGEN; do
  rm -rf "$DEST/skills/$s"
  cp -R "$OLDGEN_SRC/$s" "$DEST/skills/$s"
  echo "    COPY: $s"
done
# §6.5: 외부 플러그인 의존인 중첩 moai-content/ 하위 트리 이식 제외
rm -rf "$DEST/skills/design-system-library/moai-content"
echo "    EXCLUDE: design-system-library/moai-content (§6.5)"

# ============================================================
# 4. 헌법 (FROZEN 축자 이식 — cp로 byte-identity 보장, §8.1)
# ============================================================
echo "▸ [4/6] constitution.md FROZEN 축자 이식"
cp "$FROZEN_SRC/.claude/rules/moai/design/constitution.md" "$DEST/rules/moai/design/constitution.md"

# ============================================================
# 5. design.yaml (정본 설정 — 기본값 보존, §8.2)
# ============================================================
echo "▸ [5/6] design.yaml 정본 이식"
cp "$FROZEN_SRC/.moai/config/sections/design.yaml" "$DEST/config/design.yaml"

# ============================================================
# 6. 축소 에이전트 카탈로그 3종 (moai-code 정본 — 이미 plugin-adapted, §9.3)
#    design-handoff-coordinator는 DEPRECATE(P1) — 번들 제외(§9.2)
# ============================================================
echo "▸ [6/6] 에이전트 3종 이식"
for a in manager-spec sync-auditor builder-harness; do
  cp "$AGENT_SRC/$a.md" "$DEST/agents/$a.md"
  echo "    COPY: $a"
done

echo "✓ COPY 레이어 완료 — 신세대:5 구세대:6 헌법:1 설정:1 에이전트:3"
echo "  후속(authored, Edit/Write): SKILL.md v0.1.0 정규화(§4.5), plugin.json(§7.1),"
echo "  commands/*.md(§5), README.md(§7.3), slop ABSORB(§3.3), handoff §5.4 재설계."
