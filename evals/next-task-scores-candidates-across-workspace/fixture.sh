#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

# Three sibling repos under one workspace root: a hub carrying repos.md, and
# two implementation repos. Each is a real Git repo; none has a remote or a
# tag, so "once orders-sdk publishes v0.3.0" cannot be satisfied.
for repo in hub orders-api orders-sdk; do
  git -C "$repo" init -q -b main
  git -C "$repo" add -A
  git -C "$repo" -c user.email=eval@example.com -c user.name="Eval Fixture" \
    commit -q -m "chore: initial commit"
done
