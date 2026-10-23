#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

# A hub plus three sibling repos, each a real Git repo. No remote and no
# tag: nothing here waits on a published version.
for repo in roadmap billing-api billing-web billing-jobs; do
  git -C "$repo" init -q -b main
  git -C "$repo" add -A
  git -C "$repo" -c user.email=eval@example.com -c user.name="Eval Fixture" \
    commit -q -m "chore: initial commit"
done

# billing-api has an edit nobody committed yet.
printf '\n\ndef list_overdue_invoices():\n    return []\n' >> billing-api/src/main.py
