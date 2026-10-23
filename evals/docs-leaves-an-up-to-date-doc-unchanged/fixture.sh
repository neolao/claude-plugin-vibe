#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

commit() {
  GIT_AUTHOR_DATE="$2" GIT_COMMITTER_DATE="$2" \
    git -c user.email=t@t.test -c user.name=test commit -q -m "$1"
}

git init -q -b main
git add -A -- . ':!docs'
commit "chore: release v1.3.0" "2026-09-01T10:00:00+00:00"
git add -A -- docs
commit "docs: generate docs/architecture.md" "2026-09-02T10:00:00+00:00"
