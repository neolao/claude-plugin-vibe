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
  // TODO: render the body; only the header is written so far
  return Buffer.from(`%PDF-1.4\n${report.title}`);
}

module.exports = { exportPdf };
JS
commit "wip: add PDF export (plan rejected)"

cat > src/pdf-export.js <<'JS'
function exportPdf(report) {
  return Buffer.from(`%PDF-1.4\n${report.title}\n${report.body}`);
}

module.exports = { exportPdf };
JS
commit "feat: add PDF export for monthly reports"
