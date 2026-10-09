#!/usr/bin/env bash
# Build dist/skool-platinum.zip for uploading to claude.ai (Settings > Capabilities > Skills).
# The zip holds one folder, skool-platinum/, with SKILL.md at its root, which is the layout claude.ai expects.
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STAGE="$(mktemp -d)"
mkdir -p "$REPO_DIR/dist"
cp -R "$REPO_DIR/skill" "$STAGE/skool-platinum"
find "$STAGE" -name '.DS_Store' -delete
rm -f "$REPO_DIR/dist/skool-platinum.zip"
(cd "$STAGE" && zip -qr -X "$REPO_DIR/dist/skool-platinum.zip" skool-platinum)
rm -rf "$STAGE"
echo "Built $REPO_DIR/dist/skool-platinum.zip ($(du -h "$REPO_DIR/dist/skool-platinum.zip" | cut -f1))"
