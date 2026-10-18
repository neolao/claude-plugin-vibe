#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures/." .

git init -q
git config user.email "eval@example.com"
git config user.name "Eval Fixture"

echo ".eval-remote/" > .gitignore

git add -A
git commit -q -m "chore: initial tiny-pub-lib scaffold"
git tag v1.0.0

# The stand-in remote lives in the workspace, never a network host.
git init --bare -q .eval-remote/origin.git
git remote add origin "$PWD/.eval-remote/origin.git"
git push -q -u origin HEAD
git push -q origin v1.0.0

# A teammate pushes a commit to origin that this workspace does not have.
git clone -q .eval-remote/origin.git .eval-remote/teammate
(
  cd .eval-remote/teammate
  git config user.email "teammate@example.com"
  git config user.name "Teammate"
  echo "Teammate notes" > NOTES.md
  git add NOTES.md
  git commit -q -m "docs: add teammate notes"
  git push -q origin HEAD
)

# Local commit, not on origin: records a Fixed entry only.
cat > greet.js <<'EOF'
function greet(name) {
  return `Hello, ${name}!`;
}

module.exports = { greet };
EOF

cat > CHANGELOG.md <<'EOF'
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed

- Fixed `greet()` returning a misspelled greeting ("Helo" instead of "Hello").

## [1.0.0] - 2026-01-01

### Added

- Initial release of `greet()`.
EOF

git add -A
git commit -q -m "fix: correct greeting typo in greet()"
