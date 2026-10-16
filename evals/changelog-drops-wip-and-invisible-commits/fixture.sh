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

cat > src/pagination.js <<'JS'
function paginate(items, pageSize) {
  const pages = [];
  for (let start = 0; start < items.length; start += pageSize) {
    pages.push(items.slice(start, start + pageSize));
  }
  return pages;
}

module.exports = { paginate };
JS
commit "refactor: apply code quality fixes from vibe:review"

mkdir -p test
cat > test/pagination.test.js <<'JS'
const assert = require("node:assert");
const { paginate } = require("../src/pagination");

assert.deepStrictEqual(paginate([1, 2], 5), [[1, 2]]);
JS
commit "test: cover pagination with a single page"

cat > src/pagination.js <<'JS'
function paginate(items, pageSize) {
  const pages = [];
  for (let start = 0; start < items.length; start += pageSize) {
    pages.push(items.slice(start, start + pageSize));
  }
  if (pages.length === 0) {
    pages.push([]);
  }
  return pages;
}

module.exports = { paginate };
JS
commit "fix: keep the last page of paginated results when the list is empty"
