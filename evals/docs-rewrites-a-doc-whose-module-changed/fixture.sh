#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

commit() {
  git add -A
  GIT_AUTHOR_DATE="$2" GIT_COMMITTER_DATE="$2" \
    git -c user.email=t@t.test -c user.name=test commit -q -m "$1"
}

git init -q -b main
commit "chore: release v1.3.0 with its docs" "2026-09-01T10:00:00+00:00"

mkdir -p src/export
cat > src/export/csv.js <<'JS'
const { readWidgets } = require("../storage/store");

function exportCsv() {
  const widgets = readWidgets();
  const lines = ["name", ...widgets.map((w) => JSON.stringify(w.name))];
  console.log(lines.join("\n"));
}

module.exports = { exportCsv };
JS
cat > src/commands/index.js <<'JS'
const { listWidgets } = require("./list");
const { addWidget } = require("./add");
const { exportCsv } = require("../export/csv");

function runCommand(args) {
  const [name, ...rest] = args;
  if (name === "list") return listWidgets(rest);
  if (name === "add") return addWidget(rest[0]);
  if (name === "export") return exportCsv();
  console.error(`Unknown command: ${name}`);
}

module.exports = { runCommand };
JS
cat > CHANGELOG.md <<'MD'
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- Add `widgetcli export` to write the widgets as CSV

## [1.3.0] - 2026-09-01

### Added

- Add `widgetcli list --json` to output widgets as JSON for scripting
- Add configurable storage path via the `WIDGETCLI_HOME` environment variable

## [1.2.0] - 2026-08-01

### Added

- Initial release with `add` and `list` commands
MD
commit "feat: export the widgets as CSV" "2026-09-03T10:00:00+00:00"
