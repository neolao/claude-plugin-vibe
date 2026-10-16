#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

commit() { git add -A; git -c user.email=t@t.test -c user.name=test commit -q -m "$1"; }

cat > src/xml-export.js <<'JS'
function exportXml(rows) {
  return `<rows>${rows.map((r) => `<row>${Object.values(r).join("")}</row>`).join("")}</rows>`;
}

module.exports = { exportXml };
JS
printf '# reportkit\n\nGenerate monthly reports and export them as CSV or XML.\n' > README.md

git init -q -b main
commit "Initial commit"
git tag v1.0.0

cat > src/theme.js <<'JS'
const themes = { light: { background: "#fff" }, dark: { background: "#111" } };

function theme(name) {
  return themes[name] || themes.light;
}

module.exports = { theme };
JS
commit "Add dark mode to the report viewer"

git rm -q src/xml-export.js
commit "Remove the legacy XML export"

cat > src/exporter.js <<'JS'
function exportCsv(rows) {
  if (!rows || rows.length === 0) {
    return "";
  }
  return rows.map((r) => Object.values(r).join(",")).join("\n");
}

module.exports = { exportCsv };
JS
commit "Patch the crash when a report has no rows"

printf '# reportkit\n\nGenerate monthly reports and export them as CSV.\n' > README.md
commit "Fix typo in README"
