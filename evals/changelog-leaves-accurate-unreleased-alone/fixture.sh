#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

git init -q -b main
git add -A
git -c user.email=t@t.test -c user.name=test commit -q -m "chore: initial commit"
git tag v1.0.0

# Two user-facing commits — both already written up under [Unreleased].
cat > src/exporter.js <<'JS'
function exportCsv(rows) {
  return rows.map((r) => Object.values(r).join(",")).join("\n");
}

module.exports = { exportCsv };
JS
git add -A
git -c user.email=t@t.test -c user.name=test commit -q -m "feat: add CSV export for monthly reports"

cat > src/pagination.js <<'JS'
function paginate(items, pageSize) {
  const pages = [];
  for (let i = 0; i < items.length; i += pageSize) {
    pages.push(items.slice(i, i + pageSize));
  }
  return pages;
}

module.exports = { paginate };
JS
git add -A
git -c user.email=t@t.test -c user.name=test commit -q -m "fix: correct off-by-one error that skipped the last page of paginated results"

# Everything after this point is noise with no user-visible effect.
echo "// tidy up" >> src/index.js
git add -A
git -c user.email=t@t.test -c user.name=test commit -q -m "refactor: tidy the package entry point"

echo '{"lodash":"^4.17.21"}' > deps.lock
git add -A
git -c user.email=t@t.test -c user.name=test commit -q -m "chore: bump deps"

git checkout -q -b topic
echo "// formatting tweak" >> src/exporter.js
git add -A
git -c user.email=t@t.test -c user.name=test commit -q -m "chore: wip formatting tweak"
git checkout -q main
git merge --no-ff -q -m "Merge branch 'topic' into main" topic
