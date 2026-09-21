#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures"/. .
git init -q
git config user.email "eval@example.com"
git config user.name "Eval Runner"
git add -A
git commit -q -m "chore: initial fixture state"
