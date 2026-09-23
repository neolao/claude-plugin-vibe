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
