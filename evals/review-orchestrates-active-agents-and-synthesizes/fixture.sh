#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Copy fixture files into the run's workspace root (not a subfolder): the
# skill under test reviews "the full codebase" with no $ARGUMENTS, i.e. cwd.
cp -r "$dir/fixtures/." .

# /vibe:review's Step 6 commits on every run, so the workspace needs to be a
# real git repo with a clean initial commit for that commit to succeed.
git init -q
git config user.email "eval-fixture@example.com"
git config user.name "Eval Fixture"
git add -A
git commit -q -m "chore: initial fixture"
