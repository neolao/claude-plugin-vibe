#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

commit() { git add -A; git -c user.email=t@t.test -c user.name=test commit -q -m "$1"; }

git init -q -b main
commit "chore: initial commit"
git tag v1.9.0

cat > src/csv-export.js <<'JS'
function exportCsv(rows) {
  return rows.map((r) => Object.values(r).join(",")).join("\n");
}

module.exports = { exportCsv };
JS
commit "feat: add CSV export for monthly reports"
git tag v1.10.0

cat > src/search.js <<'JS'
function search(query, records) {
  const q = String(query).trim();
  return records.filter((r) => r.includes(q));
}

module.exports = { search };
JS
commit "fix(search): return results for queries with trailing whitespace"

cat > src/pdf-export.js <<'JS'
function exportPdf(report) {
  return Buffer.from(`%PDF-1.4\n${report.title}\n${report.body}`);
}

module.exports = { exportPdf };
JS
commit "feat(export): add PDF export for monthly reports"

cat > .ci.yml <<'YML'
build:
  cache:
    key: "$CI_COMMIT_REF_SLUG"
    paths: [node_modules/]
  script: npm test
YML
commit "chore(ci): fix flaky pipeline cache"

git checkout -q -b perf/report-list
cat > src/report-list.js <<'JS'
function listReports(reports, pageSize) {
  const index = new Map(reports.map((r) => [r.id, r]));
  return [...index.values()].slice(0, pageSize);
}

module.exports = { listReports };
JS
commit "improve: load the report list twice as fast on large accounts"
git checkout -q main
git merge --no-ff -q -m "Merge branch 'perf/report-list' into main" perf/report-list

cat > src/routes.js <<'JS'
const routes = {
  "/v1/reports": { handler: "reportsV1", deprecated: true },
  "/v2/reports": { handler: "reportsV2" },
};

module.exports = { routes };
JS
commit "deprecate: mark the /v1/reports endpoint as deprecated in favour of /v2/reports"
