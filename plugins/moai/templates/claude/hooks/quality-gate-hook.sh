#!/bin/bash
# quality-gate-hook.sh — project-level quality-gate template (Stop hook)
#
# Generated for a USER PROJECT by the /moai --project survey-driven
# meta-harness (SPEC-MOC-PM-ADVISORS-001). This template targets the
# TARGET PROJECT's own .claude/hooks/ directory — it is never invoked
# from, and never references, this plugin's own hooks/ directory
# (REQ-H-002: meta-harness generation targets the user's project
# exclusively; plugin-level hooks remain as-is).
#
# Auto-detects the project's toolchain from marker files and runs the
# matching quality gate (lint + test), mirroring the language-specific
# guidelines table in CLAUDE.md §7. Missing tools are skipped
# gracefully; projects with no recognized language marker pass
# silently. Always exits 0 — advisory, non-blocking.
#
# Manual smoke test:
#   bash plugins/moai/templates/claude/hooks/quality-gate-hook.sh

PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$PWD}"
cd "$PROJECT_DIR" 2>/dev/null || exit 0

run_if_present() {
    if command -v "$1" >/dev/null 2>&1; then
        "$@" || true
    fi
    return 0
}

if [ -f "go.mod" ]; then
    run_if_present go vet ./...
    run_if_present golangci-lint run --timeout=2m
    run_if_present go test ./...
elif [ -f "package.json" ]; then
    run_if_present eslint .
    run_if_present npm test
elif [ -f "pyproject.toml" ] || [ -f "requirements.txt" ]; then
    run_if_present ruff check .
    run_if_present pytest
elif [ -f "Cargo.toml" ]; then
    run_if_present cargo clippy
    run_if_present cargo test
fi

exit 0
