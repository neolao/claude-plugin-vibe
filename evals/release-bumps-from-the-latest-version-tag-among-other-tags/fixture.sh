#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

git init -q -b main
git config user.email "eval@example.com"
git config user.name "Eval Fixture"
git remote add origin https://github.com/example/widget-tool.git
git add -A
git commit -q -m "chore: initial commit"
git tag v1.2.3

# The fix the pending changelog entry describes, then the deployment tags
# the ops team puts on the commit they deployed.
cat > widget.sh <<'SH'
#!/bin/sh
# Prints the widgets listed in the file given as first argument, one per line.
[ -f "${1:-}" ] || exit 0
tr ',' '\n' < "$1"
SH
git add -A
git commit -q -m "fix: exit cleanly when the widget file is missing"
git tag deploy-2026-01-15
git tag vnext
