#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

# A real, local-only Git repo with no workspace hub around it.
git init -q -b main
git add -A
git -c user.email=eval@example.com -c user.name="Eval Fixture" commit -q -m "chore: initial commit"
