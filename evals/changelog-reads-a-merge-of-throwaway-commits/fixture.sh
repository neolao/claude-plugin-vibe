#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

commit() { git add -A; git -c user.email=t@t.test -c user.name=test commit -q -m "$1"; }

git init -q -b main
commit "chore: initial commit"
git tag v1.0.0

cat > src/pagination.js <<'JS'
function paginate(items, pageSize) {
  const pages = [];
  for (let i = 0; i < items.length; i += pageSize) {
    pages.push(items.slice(i, i + pageSize));
  }
  if (pages.length === 0) {
    pages.push([]);
  }
  return pages;
}

module.exports = { paginate };
JS
commit "fix: keep the last page of paginated results when the list is empty"

git checkout -q -b alice/pdf-export
cat > src/pdf-export.js <<'JS'
function exportPdf(report) {
  return Buffer.from(`%PDF-1.4\n${report.title}`);
}

module.exports = { exportPdf };
JS
commit "wip"

cat > src/pdf-export.js <<'JS'
function exportPdf(report) {
  return Buffer.from(`%PDF-1.4\n${report.title}\n${report.body}`);
}

module.exports = { exportPdf };
JS
commit "fixup"

cat > src/pdf-export.js <<'JS'
function exportPdf(report) {
  // Minimal PDF: one page, the title and the body as plain text.
  return Buffer.from(`%PDF-1.4\n${report.title}\n${report.body}`);
}

module.exports = { exportPdf };
JS
commit "typo"

git checkout -q main
git -c user.email=t@t.test -c user.name=test merge --no-ff -q -m "Merge pull request #12 from alice/pdf-export" -m "Add PDF export for monthly reports" alice/pdf-export
