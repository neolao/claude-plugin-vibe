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
git tag v1.2.3

# A fix recorded in the changelog by hand, as /vibe:fix would have done.
cat > src/config.js <<'JS'
function loadConfig(entries) {
  return Object.fromEntries(entries ?? []);
}

module.exports = { loadConfig };
JS
git add -A
git commit -q -m "fix: handle a config file with no entries"

# A feature committed without touching the changelog: only git knows it.
cat > src/export.js <<'JS'
function toCsv(rows) {
  return rows.map((row) => row.join(',')).join('\n');
}

module.exports = { toCsv };
JS
git add -A
git commit -q -m "feat: add a CSV export for monthly reports"
