#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures/." .

git init -q
git config user.email "eval@example.com"
git config user.name "Eval Fixture"
chmod +x bin/gh

# The stand-in remote lives in the workspace, so it must never be committed
# into the workspace's own history.
echo ".eval-remote/" > .gitignore

# Commit 1: the released v1.0.0 state.
git add -A
git commit -q -m "chore: initial tiny-pub-lib scaffold"
git tag v1.0.0

# origin is a GitHub URL, as the forge-release step requires, but its push
# URL is a bare repo inside the run workspace — concurrent runs never share
# it, cleanup removes it with everything else, and no network host is ever
# reached.
git init --bare -q .eval-remote/tiny-pub-lib.git
git remote add origin "https://github.com/example/tiny-pub-lib.git"
git remote set-url --push origin "$PWD/.eval-remote/tiny-pub-lib.git"
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
