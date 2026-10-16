#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures/." .

git init -q -b main
git config user.email "eval@example.com"
git config user.name "Eval Fixture"
git add -A
git commit -q -m "chore: auto run — 1 item (0 done, 0 blocked, 1 aborted)"

# A human repaired the build after the run closed.
cat > listutils.py <<'PY'
"""Small list utility functions with no external dependencies."""


def is_even(n):
    """Return True if n is an even integer."""
    return n % 2 == 0


def first_of(values):
    """Return the first value; used by callers that render a preview row."""
    return values[0]
PY
git add listutils.py
git commit -q -m "fix: restore the closing bracket in first_of"
