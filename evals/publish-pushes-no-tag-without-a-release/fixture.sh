#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures/." .

git init -q
git config user.email "eval@example.com"
git config user.name "Eval Fixture"

# The stand-in remote lives in the workspace, so it must never be committed
# into the workspace's own history.
echo ".eval-remote/" > .gitignore

# Commit 1: the released v1.0.0 state. A release candidate tag was cut
# locally before v1.0.0 and never published.
git add -A
git commit -q -m "chore: initial tiny-pub-lib scaffold"
git tag v0.9.0-rc1
git tag v1.0.0

# A local bare repo stands in for the "remote" — inside the run workspace, so
# concurrent runs never share it and cleanup removes it with everything else.
# Never a real network host. Only v1.0.0 is published.
git init --bare -q .eval-remote/origin.git
git remote add origin "$PWD/.eval-remote/origin.git"
git push -q -u origin HEAD
git push -q origin v1.0.0

# Commit 2: housekeeping with no user-visible effect and no changelog entry,
# so there is nothing to release. Kept local, ahead of origin.
cat > greet.test.js <<'JS'
const assert = require('assert');
const { greet } = require('./greet');

assert.strictEqual(greet('Ada'), 'Hello, Ada!');
console.log('greet: ok');
JS

git add -A
git commit -q -m "chore: label the test output"
