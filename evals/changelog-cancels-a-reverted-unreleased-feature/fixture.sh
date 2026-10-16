#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

commit() { git add -A; git -c user.email=t@t.test -c user.name=test commit -q -m "$1" ${2:+-m "$2"}; }

git init -q -b main
commit "chore: initial commit"
git tag v1.0.0

cat > src/pdf-export.js <<'JS'
function exportPdf(report) {
  return Buffer.from(`%PDF-1.4\n${report.title}\n${report.body}`);
}

module.exports = { exportPdf };
JS
cat > CHANGELOG.md <<'MD'
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- Export a monthly report as PDF

## [1.0.0] - 2026-06-01

### Added

- Initial release of reportkit with CSV export and basic pagination
MD
commit "feat: add PDF export for monthly reports"
feat_sha="$(git rev-parse HEAD)"

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

# The code is taken back by hand; the changelog entry is forgotten.
git rm -q src/pdf-export.js
commit "Revert \"feat: add PDF export for monthly reports\"" "This reverts commit ${feat_sha}. The PDF renderer crashes on reports over 50 pages."
