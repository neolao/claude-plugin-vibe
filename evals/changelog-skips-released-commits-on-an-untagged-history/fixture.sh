#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

commit() { git add -A; git -c user.email=t@t.test -c user.name=test commit -q -m "$1"; }

# Hold the two released features back so their commits exist in history.
mv src/exporter.js /tmp/exporter.js.$$
mv src/pagination.js /tmp/pagination.js.$$
cat > CHANGELOG.md <<'MD'
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]
MD
git init -q -b main
commit "chore: initial commit"

mv /tmp/exporter.js.$$ src/exporter.js
commit "feat: add CSV export for monthly reports"

mv /tmp/pagination.js.$$ src/pagination.js
commit "feat: add pagination to the report list"

cp "$dir/fixtures/CHANGELOG.md" CHANGELOG.md
commit "chore: release v1.0.0"
# No tag: the release was cut in the changelog only.

cat > src/pdf-export.js <<'JS'
function exportPdf(report) {
  return Buffer.from(`%PDF-1.4\n${report.title}\n${report.body}`);
}

module.exports = { exportPdf };
JS
commit "feat: add PDF export for monthly reports"

cat > src/report-list.js <<'JS'
function listReports(reports) {
  return [...reports].sort((a, b) => b.date.localeCompare(a.date));
}

module.exports = { listReports };
JS
commit "fix: sort the report list by date instead of by title"
