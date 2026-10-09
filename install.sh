#!/usr/bin/env bash
# Install the skool-platinum skill into Claude Code.
#   ./install.sh            -> ~/.claude/skills/skool-platinum  (every project)
#   ./install.sh --project  -> ./.claude/skills/skool-platinum  (only the folder you run it from)
# Re-running updates the skill and keeps your filled-in profile and competitor files.
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$REPO_DIR/skill"

if [[ "${1:-}" == "--project" ]]; then
  DEST="$(pwd)/.claude/skills/skool-platinum"
else
  DEST="$HOME/.claude/skills/skool-platinum"
fi

if [[ ! -f "$SRC/SKILL.md" ]]; then
  echo "Cannot find $SRC/SKILL.md. Run this script from inside the cloned repo." >&2
  exit 1
fi

KEEP_DIR=""
if [[ -d "$DEST" ]]; then
  KEEP_DIR="$(mktemp -d)"
  for f in context/my-skool-profile.md context/competitor-landscape.md; do
    if [[ -f "$DEST/$f" ]] && ! grep -q '^status: blank' "$DEST/$f"; then
      mkdir -p "$KEEP_DIR/$(dirname "$f")"
      cp "$DEST/$f" "$KEEP_DIR/$f"
    fi
  done
  rm -rf "$DEST"
fi

mkdir -p "$(dirname "$DEST")"
cp -R "$SRC" "$DEST"

if [[ -n "$KEEP_DIR" ]]; then
  if [[ -d "$KEEP_DIR/context" ]]; then
    cp "$KEEP_DIR"/context/*.md "$DEST/context/"
    echo "Kept your filled-in profile / competitor files."
  fi
  rm -rf "$KEEP_DIR"
fi

echo "Installed skool-platinum to $DEST"
echo "Restart Claude Code, then type: /skool-platinum onboard"
