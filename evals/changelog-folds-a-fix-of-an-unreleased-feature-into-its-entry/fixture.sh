#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

commit() { git add -A; git -c user.email=t@t.test -c user.name=test commit -q -m "$1"; }

git init -q -b main
commit "chore: initial commit"
git tag v1.0.0

cat > src/pdf-export.js <<'JS'
function exportPdf(report) {
  const lines = report.rows.map((row) => row.join("  "));
  return Buffer.from(`%PDF-1.4\n${report.title}\n${lines.join("\n")}`);
}

module.exports = { exportPdf };
JS
commit "feat: add PDF export for monthly reports"

cat > src/pdf-export.js <<'JS'
function exportPdf(report) {
  const rows = report.rows || [];
  const lines = rows.map((row) => row.join("  "));
  return Buffer.from(`%PDF-1.4\n${report.title}\n${lines.join("\n")}`);
}

module.exports = { exportPdf };
JS
commit "fix: PDF export crashes on a report with no rows"

cat > src/pagination.js <<'JS'
function paginate(items, pageSize) {
  if (items.length === 0) {
    return [[]];
  }
  const pages = [];
  for (let i = 0; i < items.length; i += pageSize) {
    pages.push(items.slice(i, i + pageSize));
  }
  return pages;
}

module.exports = { paginate };
JS
commit "fix: show an empty first page instead of no page when the report list is empty"
