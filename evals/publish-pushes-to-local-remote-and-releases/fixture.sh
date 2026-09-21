#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures/." .

git init -q
git config user.email "eval@example.com"
git config user.name "Eval Fixture"

# Commit 1: the released v1.0.0 state (greet() has a real typo bug here —
# that's fine, this commit is only ever history, never re-checked-out).
git add -A
git commit -q -m "chore: initial tiny-pub-lib scaffold"
git tag v1.0.0

# A local bare repo stands in for the "remote" — a sibling directory, never
# a real network host.
git init --bare -q ../origin.git
git remote add origin ../origin.git
git push -q -u origin HEAD
git push -q origin v1.0.0

# Commit 2: fixes the typo and records it under Unreleased > Fixed only, so
# vibe:publish's auto-decided bump is patch. Kept local, ahead of origin.
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
