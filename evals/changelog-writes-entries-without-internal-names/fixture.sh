#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

commit() { git add -A; git -c user.email=t@t.test -c user.name=test commit -q -m "$1"; }

git init -q -b main
commit "chore: initial commit"
git tag v1.0.0

cat > src/pdf-export.js <<'JS'
class ReportService {
  exportPdf(report) {
    return Buffer.from(`%PDF-1.4\n${report.title}\n${report.body}`);
  }
}

module.exports = { ReportService };
JS
commit "feat: add exportPdf() to ReportService in src/pdf-export.js"

cat > src/pagination.js <<'JS'
function paginate(items, pageSize) {
  if (pageSize <= 0) {
    return [items];
  }
  const pages = [];
  for (let i = 0; i < items.length; i += pageSize) {
    pages.push(items.slice(i, i + pageSize));
  }
  return pages;
}

module.exports = { paginate };
JS
commit "fix: guard paginate() against pageSize 0 in src/pagination.js (infinite loop)"
