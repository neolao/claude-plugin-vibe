#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

git init -q -b main
git config user.email "eval@example.com"
git config user.name "Eval Fixture"
git add -A
git commit -q -m "chore: initial commit"

# The review baseline points at the commit above.
head_hash="$(git rev-parse --short HEAD)"
mkdir -p .vibe
cat > .vibe/last-review.md <<EOT
# Last review
date: 2024-03-04
commit: ${head_hash}
EOT
git add .vibe/last-review.md
git commit -q -m "chore: record vibe:review run"

# Six feat:/fix: commits land after the baseline, interleaved with two chore:
# commits that must not be counted.
for msg in \
  "feat: add CSV export" \
  "fix: correct the total on empty carts" \
  "chore: bump lint config" \
  "feat: remember the last used filter" \
  "fix: stop losing the draft on reload" \
  "chore: reformat the README" \
  "feat: show a progress bar during export" \
  "fix: accept uppercase coupon codes"
do
  echo "# ${msg}" >> src/app.py
  git add src/app.py
  git commit -q -m "${msg}"
done
