#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

for repo in orders-api orders-sdk; do
  git -C "$repo" init -q -b main
  git -C "$repo" -c user.email="eval@example.com" -c user.name="Eval Fixture" add -A
  git -C "$repo" -c user.email="eval@example.com" -c user.name="Eval Fixture" commit -q -m "chore: initial commit"
done
