#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

# A real, local-only Git repo: no remote configured, so vibe:publish's push
# step fails fast and predictably ("no configured push destination") instead
# of hanging or silently succeeding.
git init -q -b main
git add -A
git -c user.email=eval@example.com -c user.name="Eval Runner" commit -q -m "chore: initial commit"
