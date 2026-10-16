#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

commit() { git add -A; git -c user.email=t@t.test -c user.name=test commit -q -m "$1"; }

git init -q -b main
commit "chore: initial commit"

cat > src/pdf-export.js <<'JS'
function exportPdf(report) {
  return Buffer.from(`%PDF-1.4\n${report.title}\n${report.body}`);
}

module.exports = { exportPdf };
JS
commit "feat: add PDF export for monthly reports"

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

echo '{"lodash":"^4.17.21"}' > deps.lock
commit "chore: bump deps"
