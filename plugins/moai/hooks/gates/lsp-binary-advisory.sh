#!/bin/bash
# Hook: lsp-binary-advisory
# Purpose: SessionStart advisory — warns (never blocks) when a language server
#          declared in .lsp.json matches project files but its binary is
#          missing from PATH. Non-blocking, always exit 0 (REQ-L-006/REQ-L-007).
# Trigger: SessionStart event, registered ADDITIVELY alongside dispatch.sh in
#          hooks.json (REQ-L-008 — the 5 existing gate scripts + dispatch.sh
#          stay byte-unchanged; this is a new, separate script).
#
# Manual smoke test:
#   printf '{"hook_event_name":"SessionStart"}' | PATH=/usr/bin:/bin \
#     bash plugins/moai/hooks/gates/lsp-binary-advisory.sh
# Expected: exit 0; stdout/stderr never contain the tokens "decision" or "block".
#
# HARD invariant: this script deliberately does NOT use `set -e` — every
# fallible command is defensively guarded so the script always reaches its
# final `exit 0`, regardless of missing tools (jq), missing config, or a
# stripped-down PATH.

PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$PWD}"

# Resolve plugin root: prefer ${CLAUDE_PLUGIN_ROOT}; fall back to the script's
# own location (gates/ -> hooks/ -> plugin root) when the env var is unset
# (e.g. a manual smoke test invoked directly with `bash`).
if [ -n "$CLAUDE_PLUGIN_ROOT" ]; then
    PLUGIN_ROOT="$CLAUDE_PLUGIN_ROOT"
else
    SCRIPT_DIR="$(cd "$(dirname "$0")" 2>/dev/null && pwd)"
    PLUGIN_ROOT="$(dirname "$(dirname "$SCRIPT_DIR")" 2>/dev/null)"
fi

LSP_CONFIG="${PLUGIN_ROOT}/.lsp.json"
GUIDE_POINTER="plugins/moai/references/lsp-install-guide.md"

# Consume stdin (the SessionStart hook payload) without acting on its content
# — this hook is advisory-only and does not need to parse hook_event_name.
cat >/dev/null 2>&1 || true

# Graceful degradation: jq is required to parse .lsp.json. Skip silently if
# absent — never fail, never block.
if ! command -v jq >/dev/null 2>&1; then
    exit 0
fi

if [ ! -f "$LSP_CONFIG" ]; then
    exit 0
fi

ADVISORIES=""
LANGS=$(jq -r 'keys[]' "$LSP_CONFIG" 2>/dev/null)

for lang in $LANGS; do
    BIN=$(jq -r --arg l "$lang" '.[$l].command // empty' "$LSP_CONFIG" 2>/dev/null)
    [ -z "$BIN" ] && continue

    # Binary present on PATH — nothing to advise for this language.
    if command -v "$BIN" >/dev/null 2>&1; then
        continue
    fi

    EXTS=$(jq -r --arg l "$lang" '.[$l].extensionToLanguage // {} | keys[]' "$LSP_CONFIG" 2>/dev/null)
    MATCHED=""
    for ext in $EXTS; do
        HIT=$(find "$PROJECT_DIR" -maxdepth 4 -type f -name "*${ext}" -print -quit 2>/dev/null)
        if [ -n "$HIT" ]; then
            MATCHED="yes"
            break
        fi
    done

    if [ -n "$MATCHED" ]; then
        ADVISORIES="${ADVISORIES}[moai-lsp-advisory] ${lang}: server binary '${BIN}' not found on PATH. See ${GUIDE_POINTER} for install instructions.
"
    fi
done

# Non-blocking notice on stderr only — this hook never emits stdout JSON and
# never contains the tokens "decision" or "block" (REQ-L-007 / AC-CLM-006).
if [ -n "$ADVISORIES" ]; then
    printf '%s' "$ADVISORIES" >&2
fi

exit 0
