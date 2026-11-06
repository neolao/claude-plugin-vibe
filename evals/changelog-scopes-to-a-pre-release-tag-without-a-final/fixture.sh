#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

commit() { git add -A; git -c user.email=t@t.test -c user.name=test commit -q -m "$1"; }

git init -q -b main
commit "chore: initial commit"
git tag v1.2.0

cat > src/exporter.js <<'JS'
function exportCsv(rows) {
  return rows.map((r) => Object.values(r).join(",")).join("\n");
}

module.exports = { exportCsv };
JS
commit "feat: add CSV export for monthly reports"
git tag v1.3.0-rc.1

cat > src/pdf-export.js <<'JS'
function exportPdf(report) {
  return Buffer.from(`%PDF-1.4\n${report.title}\n${report.body}`);
}

module.exports = { exportPdf };
JS
commit "feat: add PDF export for monthly reports"
