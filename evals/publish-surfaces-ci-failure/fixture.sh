#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures/." .

git init -q -b main
git config user.email "eval@example.com"
git config user.name "Eval Fixture"
git remote add origin "https://github.com/example/fixture-app.git"
git add -A
git commit -q -m "chore: initial commit"

# Fake the upstream-tracking ref so this commit already reads as "pushed"
# to `git log @{u}..`, without vibe:publish's Step 1 ever needing to
# actually reach a real github.com host. Step 1 is not what this eval is
# about — see case.yaml.
git update-ref refs/remotes/origin/main HEAD
git branch -q --set-upstream-to=origin/main main

sha="$(git rev-parse HEAD)"
sed -i "s/__SHA__/$sha/g" bin/gh
chmod +x bin/gh
