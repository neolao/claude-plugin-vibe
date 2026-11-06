#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

commit() { git add -A; git -c user.email=t@t.test -c user.name=test commit -q -m "$1"; }

git init -q -b main
commit "chore: initial commit"
git tag v1.2.0

cat > src/pdf-export.js <<'JS'
function exportPdf(report) {
  return Buffer.from(`%PDF-1.4\n${report.title}\n${report.body}`);
}

module.exports = { exportPdf };
JS
commit "feat: add PDF export for monthly reports"
# The tags the ops team puts on the commit they deployed.
git tag deploy-2026-10-30
git tag vnext

cat > src/report-list.js <<'JS'
function listReports(reports) {
  return [...reports].sort((a, b) => b.date.localeCompare(a.date));
}

module.exports = { listReports };
JS
commit "fix: sort the report list by date instead of by title"
