#!/usr/bin/env bash
#
# plugins/moai/scripts/scaffold.sh
# MoAI Layer-2 project scaffolder — copies the template payload into a target
# project directory with deterministic cp + sed token substitution.
#
# @MX:ANCHOR: [AUTO] token-set + output-tree contract
#   Tokens substituted: {{PROJECT_NAME}}, {{VERSION}}, {{DATE}}, {{PROJECT_USER_NAME}}
#   Output tree: <target>/{CLAUDE.md,
#                          .claude/{rules/moai/** (61 files), settings.json},
#                          .moai/config/sections/** (27 yaml)}
# @MX:REASON: deterministic generation contract (cp+sed only — no LLM per-file copy,
#   REQ-MV2-013) is the premise for /moai:project wiring and the T2 commit path
#   (Web/remote persona auto-activation via the committed settings.json).
#
# @MX:WARN: [AUTO] settings.json preserve-merge + backup / --dry-run / user-owned preserve zone
# @MX:REASON: user-settings destruction risk — additive merge invariant (REQ-MV2-014):
#   NEVER clobber existing target keys (e.g. model); ADD outputStyle + extraKnownMarketplaces
#   + enabledPlugins. --dry-run writes zero files. User-owned namespaces (harness-*,
#   agents/local/, evaluator-profiles/) are never overwritten even if present in target.
#
# Exit codes: 0 = success / dry-run / no-op; 2 = usage error; 1 = hard error.

set -euo pipefail

main() {
  local SCRIPT_DIR PLUGIN_ROOT TEMPLATES_DIR
  SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  PLUGIN_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
  TEMPLATES_DIR="$PLUGIN_ROOT/templates"

  # --- parse args ---
  local dry_run=0 target="" opt_name="" opt_version="" opt_user=""
  while [[ $# -gt 0 ]]; do
    case "$1" in
      --dry-run) dry_run=1; shift ;;
      --name)    opt_name="${2:-}"; shift 2 ;;
      --version) opt_version="${2:-}"; shift 2 ;;
      --user)    opt_user="${2:-}"; shift 2 ;;
      -h|--help) print_usage; return 0 ;;
      --)        shift; break ;;
      -*)        echo "scaffold.sh: unknown option: $1" >&2; print_usage >&2; return 2 ;;
      *)         target="$1"; shift ;;
    esac
  done
  if [[ $# -gt 0 && -z "$target" ]]; then
    target="$1"; shift || true
  fi

  if [[ -z "$target" ]]; then
    echo "scaffold.sh: error: target directory is required" >&2
    print_usage >&2
    return 2
  fi

  if [[ ! -d "$TEMPLATES_DIR" ]]; then
    echo "scaffold.sh: error: templates dir not found: $TEMPLATES_DIR" >&2
    return 1
  fi

  # --- defaults ---
  [[ -z "$opt_version" ]] && opt_version="0.1.0"
  if [[ -z "$opt_name" ]]; then
    opt_name="$(basename "$target")"
  fi
  if [[ -z "$opt_user" ]]; then
    if [[ -n "${USER:-}" ]]; then
      opt_user="$USER"
    else
      opt_user="$(git config user.name 2>/dev/null || true)"
    fi
  fi
  local date_today
  date_today="$(date +%Y-%m-%d)"

  # --- build manifest (src, dst, mode) ---
  # mode: "copy" = cp + sed token substitution; "merge" = jq preserve-merge (settings.json)
  local -a m_src=() m_dst=() m_mode=()
  local src rel mapped dst mode
  while IFS= read -r -d '' src; do
    rel="${src#"$TEMPLATES_DIR"/}"
    mapped="$(map_dest "$target" "$rel")"
    dst="${mapped%%$'\t'*}"
    mode="${mapped##*$'\t'}"
    if is_user_owned "$dst"; then
      continue
    fi
    m_src+=("$src"); m_dst+=("$dst"); m_mode+=("$mode")
  done < <(find "$TEMPLATES_DIR" -type f -print0)

  # --- dry-run: print plan, write nothing, exit 0 ---
  if [[ "$dry_run" -eq 1 ]]; then
    echo "scaffold.sh --dry-run (no files will be written)"
    echo "  target:       $target"
    echo "  project_name: $opt_name"
    echo "  version:      $opt_version"
    echo "  date:         $date_today"
    echo "  user_name:    ${opt_user:-<empty>}"
    echo "  tokens:       {{PROJECT_NAME}} {{VERSION}} {{DATE}} {{PROJECT_USER_NAME}}"
    echo "  files planned: ${#m_src[@]}"
    echo "---"
    local idx
    for ((idx = 0; idx < ${#m_src[@]}; idx++)); do
      printf '  [%s] %s\n        -> %s\n' "${m_mode[$idx]}" "${m_src[$idx]}" "${m_dst[$idx]}"
    done
    echo "---"
    echo "dry-run complete. Re-run without --dry-run to apply."
    return 0
  fi

  # --- real run: require jq for the settings.json preserve-merge ---
  if ! command -v jq >/dev/null 2>&1; then
    echo "scaffold.sh: error: jq is required for settings.json preserve-merge but not found in PATH" >&2
    return 1
  fi

  mkdir -p "$target"
  local timestamp
  timestamp="$(date +%Y%m%dT%H%M%S)"
  local n_copied=0 n_merged=0 n_backed_up=0

  echo "Scaffolding MoAI Layer-2 into: $target"
  echo "  project_name: $opt_name | version: $opt_version | date: $date_today | user: ${opt_user:-<empty>}"

  local i rel bdir tmp_tmpl
  for ((i = 0; i < ${#m_src[@]}; i++)); do
    src="${m_src[$i]}"
    dst="${m_dst[$i]}"
    mode="${m_mode[$i]}"

    mkdir -p "$(dirname "$dst")"

    case "$mode" in
      copy)
        if [[ -f "$dst" ]]; then
          backup_file "$target" "$timestamp" "$dst"
          n_backed_up=$((n_backed_up + 1))
        fi
        substitute_tokens "$opt_name" "$opt_version" "$date_today" "$opt_user" < "$src" > "$dst"
        n_copied=$((n_copied + 1))
        ;;
      merge)
        if [[ -f "$dst" ]]; then
          backup_file "$target" "$timestamp" "$dst"
          n_backed_up=$((n_backed_up + 1))
          # preserve-merge: existing keys survive, template keys added/overwritten
          tmp_tmpl="$(mktemp)"
          substitute_tokens "$opt_name" "$opt_version" "$date_today" "$opt_user" < "$src" > "$tmp_tmpl"
          jq -s '.[0] * .[1]' "$dst" "$tmp_tmpl" > "$dst.new"
          mv "$dst.new" "$dst"
          rm -f "$tmp_tmpl"
        else
          substitute_tokens "$opt_name" "$opt_version" "$date_today" "$opt_user" < "$src" > "$dst"
        fi
        n_merged=$((n_merged + 1))
        ;;
    esac
  done

  echo ""
  echo "Done. copied: $n_copied, merged: $n_merged, backed up: $n_backed_up."
  echo ""
  cat <<'POSTINSTALL'
MoAI Layer-2 scaffolding complete.

What was placed:
  - CLAUDE.md                         (MoAI execution directive)
  - .claude/rules/moai/**             (61 rule files)
  - .claude/settings.json             (preserve-merged: outputStyle + marketplace + plugin)
  - .moai/config/sections/*.yaml      (27 config sections, tokens substituted)

Next steps:
  1. Review CLAUDE.md and .moai/config/sections/*.yaml for your project.
  2. The plugin "moai" is enabled via .claude/settings.json (outputStyle: moai:MoAI).

Note (issue #63028): In the first cloud/web session the plugin persona may appear
inactive until the marketplace clone completes. If /moai:plan or the moai: persona
do not resolve on first connect, reconnect the session — the market clone can lag
behind session start and resolves on reconnection.
POSTINSTALL
}

print_usage() {
  cat <<'USAGE'
Usage: scaffold.sh [--dry-run] [--name NAME] [--version VER] [--user USER] <target-dir>

Copies the MoAI Layer-2 template payload into <target-dir> with token substitution.

Options:
  --dry-run       Print the scaffolding plan; write nothing to disk.
  --name NAME     Project name (default: basename of target-dir).
  --version VER   Project version (default: 0.1.0).
  --user USER     User name for config sections (default: $USER or git user.name).
  -h, --help      Show this help.

Tokens substituted: {{PROJECT_NAME}}, {{VERSION}}, {{DATE}}, {{PROJECT_USER_NAME}}
USAGE
}

# Escape a string for safe use as a sed pipe-delimited (s|||g) replacement.
sed_safely() {
  local s="$1"
  s="${s//\\/\\\\}"
  s="${s//&/\\&}"
  s="${s//|/\\|}"
  printf '%s' "$s"
}

# Apply all 4 token substitutions from stdin to stdout.
# Args: project_name version date user_name
substitute_tokens() {
  sed \
    -e "s|{{PROJECT_NAME}}|$(sed_safely "$1")|g" \
    -e "s|{{VERSION}}|$(sed_safely "$2")|g" \
    -e "s|{{DATE}}|$(sed_safely "$3")|g" \
    -e "s|{{PROJECT_USER_NAME}}|$(sed_safely "$4")|g"
}

# Map a template-relative path to "<dst>\t<mode>".
# Args: target_dir template_rel_path
map_dest() {
  local t="$1" rel="$2"
  case "$rel" in
    CLAUDE.md)
      printf '%s\t%s\n' "$t/CLAUDE.md" "copy" ;;
    claude/settings.project.json)
      printf '%s\t%s\n' "$t/.claude/settings.json" "merge" ;;
    claude/*)
      printf '%s\t%s\n' "$t/.claude/${rel#claude/}" "copy" ;;
    moai/*)
      printf '%s\t%s\n' "$t/.moai/${rel#moai/}" "copy" ;;
    *)
      printf '%s\t%s\n' "$t/$rel" "copy" ;;
  esac
}

# Return 0 (true) if a dest path is in a user-owned preserve namespace.
is_user_owned() {
  case "$1" in
    */harness-*/*|*/agents/local/*|*/evaluator-profiles/*)
      return 0 ;;
  esac
  return 1
}

# Back up an existing target file into .moai-backups/<timestamp>/<rel>.
# Args: target_dir timestamp dst_file
backup_file() {
  local t="$1" ts="$2" d="$3"
  local rel bdir
  rel="${d#"$t"/}"
  bdir="$t/.moai-backups/$ts/$(dirname "$rel")"
  mkdir -p "$bdir"
  cp -p "$d" "$bdir/$(basename "$rel")"
}

main "$@"
