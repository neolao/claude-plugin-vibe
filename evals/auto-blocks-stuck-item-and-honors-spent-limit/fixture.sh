#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "$dir/fixtures/." .

git init -q -b main
git config user.email "eval@example.com"
git config user.name "Eval Fixture"
git add -A
git commit -q -m "chore: auto run — start 003"

# Work in progress on 003 when the session died, never committed.
cat > test_last_of.py <<'PY'
import unittest

from listutils import last_of


class TestLastOf(unittest.TestCase):
    def test_returns_the_last_value(self):
        self.assertEqual(last_of([7, 8, 9]), 9)
PY
cat >> listutils.py <<'PY'


def last_of(values):
    """Return the last value; used by callers that render a summary row."""
PY
