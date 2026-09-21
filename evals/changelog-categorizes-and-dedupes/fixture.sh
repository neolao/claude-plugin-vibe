#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

git init -q -b main
git add -A
git -c user.email=t@t.test -c user.name=test commit -q -m "chore: initial commit"
git tag v1.0.0

cat > src/exporter.js <<'EOF'
function exportCsv(rows) {
  return rows.map((r) => Object.values(r).join(",")).join("\n");
}

module.exports = { exportCsv };
EOF
git add -A
git -c user.email=t@t.test -c user.name=test commit -q -m "feat: add CSV export for monthly reports"

cat > src/pagination.js <<'EOF'
function paginate(items, pageSize) {
  const pages = [];
  for (let i = 0; i < items.length; i += pageSize) {
    pages.push(items.slice(i, i + pageSize));
  }
  return pages;
}

module.exports = { paginate };
EOF
git add -A
git -c user.email=t@t.test -c user.name=test commit -q -m "fix: correct off-by-one error that skipped the last page of paginated results"

cat > src/render.js <<'EOF'
function renderReport(report) {
  return `${report.title}\n${report.body}`;
}

module.exports = { renderReport };
EOF
git add -A
git -c user.email=t@t.test -c user.name=test commit -q -m "refactor: simplify the report rendering pipeline"

git rm -q src/xml-export.js
git -c user.email=t@t.test -c user.name=test commit -q -m "remove: drop the legacy XML export format"

cat > src/search.js <<'EOF'
function search(query, records) {
  const safeQuery = String(query).replace(/[^\w\s]/g, "");
  return records.filter((r) => r.includes(safeQuery));
}

module.exports = { search };
EOF
git add -A
git -c user.email=t@t.test -c user.name=test commit -q -m "security: sanitize user input in the search endpoint to prevent injection"

echo '{"lodash":"^4.17.21"}' > deps.lock
git add -A
git -c user.email=t@t.test -c user.name=test commit -q -m "chore: bump deps"

git checkout -q -b topic
echo "// formatting tweak" >> src/render.js
git add -A
git -c user.email=t@t.test -c user.name=test commit -q -m "chore: wip formatting tweak"
git checkout -q main
git merge --no-ff -q -m "Merge branch 'topic' into main" topic
