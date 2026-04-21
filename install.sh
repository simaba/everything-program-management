#!/usr/bin/env bash
# install.sh — register everything-program-management with Claude Code.
#
# Behavior:
#   - Detects this repo's path (the directory containing this script).
#   - Symlinks the repo's skills/, agents/, commands/, and rules/ into
#     ~/.claude/ so Claude Code picks them up on next launch.
#   - Optionally vendors the python helpers into ~/.local/bin/.
#   - Idempotent: safe to re-run after `git pull`.
#
# Flags:
#   --dry-run   Show what would happen, change nothing.
#   --user      Install into ~/.claude (default).
#   --project   Install into ./.claude in the current working directory
#               (use when you want the plugin scoped to one repo).
#   --no-bin    Skip linking python helpers.
#   --uninstall Remove symlinks created by a prior install.
#
# Requires: bash, ln, mkdir. Python 3.10+ for the helper scripts (PyYAML,
# jsonschema). The plugin itself does not need Python at runtime.

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_BASE="${HOME}/.claude"
LINK_BIN=1
DRY_RUN=0
UNINSTALL=0

log() { printf '[install] %s\n' "$*"; }
run() {
  if [[ "${DRY_RUN}" -eq 1 ]]; then
    printf '[dry-run] %s\n' "$*"
  else
    eval "$@"
  fi
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run)   DRY_RUN=1; shift ;;
    --user)      TARGET_BASE="${HOME}/.claude"; shift ;;
    --project)   TARGET_BASE="$(pwd)/.claude"; shift ;;
    --no-bin)    LINK_BIN=0; shift ;;
    --uninstall) UNINSTALL=1; shift ;;
    -h|--help)
      sed -n '2,22p' "$0"
      exit 0 ;;
    *)
      printf 'Unknown flag: %s\n' "$1" >&2
      exit 2 ;;
  esac
done

link_dir() {
  local src="$1" dst="$2" name
  name="$(basename "$src")"
  if [[ "${UNINSTALL}" -eq 1 ]]; then
    if [[ -L "${dst}/${name}" ]]; then
      run "rm '${dst}/${name}'"
      log "removed ${dst}/${name}"
    fi
    return
  fi
  run "mkdir -p '${dst}'"
  if [[ -e "${dst}/${name}" && ! -L "${dst}/${name}" ]]; then
    log "skip ${dst}/${name} — exists and is not a symlink (won't clobber)"
    return
  fi
  run "ln -sfn '${src}' '${dst}/${name}'"
  log "linked ${dst}/${name} -> ${src}"
}

log "repo:   ${REPO_DIR}"
log "target: ${TARGET_BASE}"
[[ "${DRY_RUN}" -eq 1 ]] && log "mode:   dry-run"
[[ "${UNINSTALL}" -eq 1 ]] && log "mode:   uninstall"

# Per-surface symlinks. We link directories rather than individual files so
# `git pull` is enough to refresh content.
link_dir "${REPO_DIR}/skills"   "${TARGET_BASE}"
link_dir "${REPO_DIR}/agents"   "${TARGET_BASE}"
link_dir "${REPO_DIR}/commands" "${TARGET_BASE}"
link_dir "${REPO_DIR}/rules"    "${TARGET_BASE}"

# Plugin manifest — Claude Code expects .claude-plugin/plugin.json to live
# alongside the install root. Symlink it so the marketplace entry resolves.
if [[ "${UNINSTALL}" -eq 0 ]]; then
  run "mkdir -p '${TARGET_BASE}/.claude-plugin'"
  run "ln -sfn '${REPO_DIR}/.claude-plugin/plugin.json' '${TARGET_BASE}/.claude-plugin/everything-program-management.json'"
  log "registered plugin manifest"
fi

# Python helpers (optional, off via --no-bin).
if [[ "${LINK_BIN}" -eq 1 && "${UNINSTALL}" -eq 0 ]]; then
  BIN_DIR="${HOME}/.local/bin"
  run "mkdir -p '${BIN_DIR}'"
  run "ln -sfn '${REPO_DIR}/scripts/raid_cli.py' '${BIN_DIR}/raid'"
  run "ln -sfn '${REPO_DIR}/scripts/decision_journal_review.py' '${BIN_DIR}/decision-journal-review'"
  log "linked helpers into ${BIN_DIR} (raid, decision-journal-review)"
  log "ensure ${BIN_DIR} is on your PATH"
fi

if [[ "${UNINSTALL}" -eq 1 ]]; then
  log "uninstall complete"
else
  log "install complete — restart Claude Code to pick up new skills/agents/commands"
fi
