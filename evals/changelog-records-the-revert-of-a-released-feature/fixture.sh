#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

commit() { git add -A; git -c user.email=t@t.test -c user.name=test commit -q -m "$1" ${2:+-m "$2"}; }

# 1.0.0: no PDF export yet.
mv src/pdf-export.js /tmp/pdf-export.js.$$
cat > CHANGELOG.md <<'MD'
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

## [1.0.0] - 2026-06-01

### Added

- Initial release of reportkit with CSV export and basic pagination
MD
git init -q -b main
commit "chore: initial commit"
git tag v1.0.0

# The feature lands with its own entry, then ships in 1.1.0.
mv /tmp/pdf-export.js.$$ src/pdf-export.js
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

cp "$dir/fixtures/CHANGELOG.md" CHANGELOG.md
commit "chore: release v1.1.0"
git tag v1.1.0

# After the release, the feature is taken back.
git rm -q src/pdf-export.js
commit "Revert \"feat: add PDF export for monthly reports\"" "This reverts commit ${feat_sha}. The PDF renderer crashes on reports over 50 pages."
