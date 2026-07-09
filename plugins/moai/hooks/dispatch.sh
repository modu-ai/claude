#!/usr/bin/env bash
# dispatch.sh — unified hook dispatcher for the moai plugin
# SPEC-MOC-PLUGIN-MOAI-V2-001 · Milestone M3 (REQ-MV2-009 / 010 / 011 / 012)
#
# All 20 hook events in hooks.json route here as: dispatch.sh <PascalCaseEvent>
# Per event + environment, the dispatcher decides:
#   (1) Web/remote session ($CLAUDE_CODE_REMOTE=true) → skip binary probe, gate-only mode
#   (2) moai binary present                  → exec moai hook <kebab>  (T3 native activation)
#   (3) event has a gate mapping in gates/   → run that gate           (T1/T2/Web fallback)
#   (4) no mapping                           → silent exit 0           (fail-open)
#
# Every exit path is exit 0 (C-3 fail-open; death-spiral prevention). The plugin
# never blocks user flow via exit code; gates convey decisions via stdout JSON,
# which Claude Code reads on the dispatcher's exit 0.

# @MX:ANCHOR: [AUTO] 20-event fan-in entrypoint — hooks.json routes every event here
# @MX:REASON: invariant contract: event-name → gate mapping + fail-open; all 20 hook events depend on this single router

set +e

event="${1:-}"   # PascalCase event name (the Claude Code hooks.json key)

# stderr sink for the T3 native path (canonical ADK pattern — keeps moai stderr out of hook output)
MOAI_HOOK_STDERR_LOG="${MOAI_HOOK_STDERR_LOG:-$HOME/.moai/logs/hook-stderr.log}"
mkdir -p "$(dirname "$MOAI_HOOK_STDERR_LOG")" 2>/dev/null || true

# @MX:WARN: [AUTO] $CLAUDE_CODE_REMOTE branch + final exit 0 — branch error wastes Web sessions on binary probe or blocks user flow
# @MX:REASON: Web/remote sessions cannot install the moai binary (probe is pure waste); any non-zero exit blocks the user — death-spiral prevention contract (C-3 / REQ-MV2-012)

# (1) Web / remote session → gate-only mode, skip binary probe (REQ-MV2-011)
if [ "$CLAUDE_CODE_REMOTE" != "true" ]; then
  # (2) moai binary present → T3 native activation (REQ-MV2-010 ①)
  if command -v moai >/dev/null 2>&1; then
    # Translate PascalCase event → moai kebab-case subcommand (canonical ADK handle-*.sh.tmpl pattern)
    case "$event" in
      SessionStart)         kebab="session-start" ;;
      PreCompact)           kebab="compact" ;;            # moai special: compact (not pre-compact)
      SessionEnd)           kebab="session-end" ;;
      PreToolUse)           kebab="pre-tool" ;;
      PostToolUse)          kebab="post-tool" ;;
      Stop)                 kebab="stop" ;;
      SubagentStop)         kebab="subagent-stop" ;;
      PostToolUseFailure)   kebab="post-tool-failure" ;;
      SubagentStart)        kebab="subagent-start" ;;
      UserPromptSubmit)     kebab="user-prompt-submit" ;;
      TeammateIdle)         kebab="teammate-idle" ;;
      TaskCompleted)        kebab="task-completed" ;;
      ConfigChange)         kebab="config-change" ;;
      StopFailure)          kebab="stop-failure" ;;
      PostCompact)          kebab="post-compact" ;;
      InstructionsLoaded)   kebab="instructions-loaded" ;;
      CwdChanged)           kebab="cwd-changed" ;;
      FileChanged)          kebab="file-changed" ;;
      PermissionDenied)     kebab="permission-denied" ;;
      PermissionRequest)    kebab="permission-request" ;;
      *)                    kebab="" ;;
    esac
    if [ -n "$kebab" ]; then
      exec moai hook "$kebab" 2>>"$MOAI_HOOK_STDERR_LOG"
      # exec replaces this process; moai owns hook semantics + exit code (exits 0 for hook events)
    fi
  fi
fi

# (3) Event → gate mapping (REQ-MV2-010 ②). Gate-only fallback (binary absent / Web remote).
# Gates live alongside this script in gates/.
gate=""
case "$event" in
  PostToolUse)
    gate="status-transition-ownership.sh" ;;   # ownership-matrix check (Write|Edit on SPEC body)
  Stop)
    gate="sync-phase-quality-gate.sh" ;;       # sync-phase lint + test + coverage gate
  TaskCompleted)
    gate="team-ac-verify.sh" ;;                # team-mode AC verify (dormant unless team.enabled)
  PreToolUse)
    gate="gateguard-fact-force.sh" ;;          # first-edit investigation advisory (DP-2 vendor)
  *)
    gate="" ;;                                  # unmapped → fail-open
esac

if [ -n "$gate" ]; then
  script_dir="$(cd "$(dirname "$0")" 2>/dev/null && pwd)"
  gate_path="$script_dir/gates/$gate"
  if [ -f "$gate_path" ]; then
    # Run gate; its stdout (JSON decision) flows to Claude Code. Dispatcher forces exit 0.
    bash "$gate_path"
    exit 0
  fi
fi

# (4) No mapping or gate missing → silent fail-open (REQ-MV2-010 ③ / REQ-MV2-012)
# Drain stdin non-blocking (parity with the retired handle-*.sh stubs)
cat >/dev/null 2>&1 || true
exit 0
