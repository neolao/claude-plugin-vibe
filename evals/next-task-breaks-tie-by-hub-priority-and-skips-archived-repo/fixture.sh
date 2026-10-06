#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

# A hub plus three sibling repos. billing-api has a real local remote with
# the v0.5.0 tag pushed, so the version wait of billing-web 001 is satisfiable.
# The remote lives inside the workspace (and is not a repo directory itself).
for repo in hub billing-api billing-web legacy-batch; do
  git -C "$repo" init -q -b main
  git -C "$repo" add -A
  git -C "$repo" -c user.email=eval@example.com -c user.name="Eval Fixture" \
    commit -q -m "chore: initial commit"
done
mkdir -p .remotes
git init -q --bare -b main .remotes/billing-api.git
git -C billing-api remote add origin ../.remotes/billing-api.git
git -C billing-api tag v0.5.0
git -C billing-api push -q origin main v0.5.0
