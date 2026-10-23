#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

git init -q -b main
git config user.email "eval@example.com"
git config user.name "Eval Fixture"
git remote add origin https://github.com/example/fixture-app.git
git add -A
git commit -q -m "chore: initial commit"

cat > src/export.js <<'JS'
function toCsv(rows) {
  return rows.map((row) => row.join(',')).join('\n');
}

module.exports = { toCsv };
JS
git add -A
git commit -q -m "feat: add a CSV export for monthly reports"
