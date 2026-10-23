#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .

git init -q -b main
git config user.email "eval@example.com"
git config user.name "Eval Fixture"
git remote add origin https://github.com/example/fixture-app.git
git add -A
git commit -q -m "chore: initial commit"
git tag v1.2.3

# The only commit since the tag: CI housekeeping, nothing a user can see.
cat > .github/workflows/ci.yml <<'YML'
name: ci
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
      - run: npm test
YML
git add -A
git commit -q -m "ci: pin the Node version used by the test workflow"
