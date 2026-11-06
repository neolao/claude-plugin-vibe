#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

commit() { git add -A; git -c user.email=t@t.test -c user.name=test commit -q -m "$1"; }

git init -q -b main
commit "chore: initial commit"
git tag v1.0.0

cat > src/exporter.js <<'JS'
function exportCsv(rows) {
  return rows.map((r) => Object.values(r).join(",")).join("\n");
}

module.exports = { exportCsv };
JS
commit "feat: add CSV export for monthly reports"
git tag v1.1.0

cat > src/report-list.js <<'JS'
function listReports(reports) {
  return [...reports].sort((a, b) => b.date.localeCompare(a.date));
}

module.exports = { listReports };
JS
commit "fix: sort the report list by date instead of by title"
