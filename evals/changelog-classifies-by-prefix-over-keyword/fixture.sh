#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

commit() { git add -A; git -c user.email=t@t.test -c user.name=test commit -q -m "$1"; }

git init -q -b main
commit "chore: initial commit"
git tag v1.0.0

cat > src/auth.js <<'JS'
function requireSecondFactor(user, code) {
  return user.totpSecret ? verifyTotp(user.totpSecret, code) : true;
}

function verifyTotp(secret, code) {
  return String(code).length === 6;
}

module.exports = { requireSecondFactor };
JS
commit "feat: add two-factor auth to the login page"

cat > src/session.js <<'JS'
const sessions = new Map();

function logout(userId) {
  for (const [id, session] of sessions) {
    if (session.userId === userId) {
      sessions.delete(id);
    }
  }
}

module.exports = { sessions, logout };
JS
commit "fix: remove stale sessions that kept users signed in after logout"

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
commit "Monday changes"
