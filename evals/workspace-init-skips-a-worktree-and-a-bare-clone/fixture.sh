#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

# One real sibling, orders-api. Next to it: a linked worktree of that same
# repo (its .git is a file), a bare clone kept as a local mirror (no working
# tree), and a plain folder of notes (no .git at all).
git -C orders-api init -q -b main
git -C orders-api -c user.email="eval@example.com" -c user.name="Eval Fixture" add -A
git -C orders-api -c user.email="eval@example.com" -c user.name="Eval Fixture" commit -q -m "chore: initial commit"
git -C orders-api worktree add -q ../orders-api-hotfix -b hotfix
git clone -q --bare orders-api mirror.git
