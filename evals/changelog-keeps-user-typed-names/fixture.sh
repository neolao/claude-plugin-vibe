#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

commit() { git add -A; git -c user.email=t@t.test -c user.name=test commit -q -m "$1"; }

git init -q -b main
commit "chore: initial commit"
git tag v1.0.0

cat > src/cli.js <<'JS'
const { exportCsv } = require("./exporter");

function run(argv, report) {
  if (argv.includes("--json")) {
    return JSON.stringify(report);
  }
  return exportCsv(report.rows);
}

module.exports = { run };
JS
commit "feat: add the --json flag to the report command"

cat > src/routes.js <<'JS'
const routes = {
  "/v1/reports": { handler: "reportsV1", deprecated: true },
  "/v2/reports": { handler: "reportsV2" },
};

module.exports = { routes };
JS
commit "deprecate: the /v1/reports endpoint in favour of /v2/reports"
