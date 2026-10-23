#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

# Two real siblings. orders-api carries a nested repo under vendor/ (its own
# .git/ directory), which belongs to orders-api, not to the workspace.
git -C orders-api/vendor/pricing-lib init -q -b main
git -C orders-api/vendor/pricing-lib -c user.email="eval@example.com" -c user.name="Eval Fixture" add -A
git -C orders-api/vendor/pricing-lib -c user.email="eval@example.com" -c user.name="Eval Fixture" commit -q -m "chore: initial commit"
for repo in orders-api orders-web; do
  git -C "$repo" init -q -b main
  git -C "$repo" -c advice.addEmbeddedRepo=false -c user.email="eval@example.com" -c user.name="Eval Fixture" add -A
  git -C "$repo" -c user.email="eval@example.com" -c user.name="Eval Fixture" commit -q -m "chore: initial commit"
done
