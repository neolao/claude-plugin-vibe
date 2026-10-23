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

# Commit 1: the released v1.0.0 state (greet() has a real typo bug here and
# passes names through untouched; this commit is only ever history, never
# re-checked-out).
git add -A
git commit -q -m "chore: initial tiny-pub-lib scaffold"
git tag v1.0.0

# A local bare repo stands in for the "remote" — inside the run workspace, so
# concurrent runs never share it and cleanup removes it with everything else.
# Never a real network host.
git init --bare -q .eval-remote/origin.git
git remote add origin "$PWD/.eval-remote/origin.git"
git push -q -u origin HEAD
git push -q origin v1.0.0

# Commit 2: fixes the typo and strips control characters from names, recorded
# under Unreleased > Fixed and Unreleased > Security. Kept local, ahead of
# origin.
cat > greet.js <<'JS'
function greet(name) {
  const safeName = name.replace(/[\u0000-\u001f\u007f]/g, '');
  return `Hello, ${safeName}!`;
}

module.exports = { greet };
JS

cat > CHANGELOG.md <<'MD'
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed

- Fixed `greet()` returning a misspelled greeting ("Helo" instead of "Hello").

### Security

- Control characters are stripped from names before they are greeted.

## [1.0.0] - 2026-01-01

### Added

- Initial release of `greet()`.
MD

git add -A
git commit -q -m "fix: correct the greeting typo and strip control characters from names"
