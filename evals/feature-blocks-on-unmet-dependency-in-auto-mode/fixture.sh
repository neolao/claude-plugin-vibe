#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures/." .
git init -q -b main
git config user.email "eval@example.com"
git config user.name "Eval Fixture"
git add -A
git commit -q -m "chore: initial fixture state"
