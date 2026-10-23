#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

# A hub plus two sibling repos, each a real Git repo with no remote and no
# tag: "once orders-sdk publishes v0.3.0" cannot be satisfied, and a push
# from orders-api fails fast ("no configured push destination").
for repo in roadmap orders-api orders-sdk; do
  git -C "$repo" init -q -b main
  git -C "$repo" add -A
  git -C "$repo" -c user.email=eval@example.com -c user.name="Eval Fixture" \
    commit -q -m "chore: initial commit"
done
