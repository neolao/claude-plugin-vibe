---
type: llm
focus: last_message
criteria: |
  `freezegun` is declared in `[project] dependencies` of
  fixtures/pyproject.toml, but only fixtures/tests/test_pricing.py — a
  test outside the scope — imports it.
  PASS if the reported findings include a `Misplaced` finding on
  `freezegun` that names fixtures/tests/ (or test_pricing.py) as its only
  importer and suggests moving it to the `dev` extra.
  FAIL if `freezegun` is not flagged, is flagged as `Unused` (never
  imported) instead of `Misplaced`, or the finding names no test outside
  the scope.
weight: 1
---

Reports `freezegun`, a runtime dependency only the tests import, as a
Misplaced finding. The tests sit outside fixtures/orders/: an agent that
greps only the scope calls it unused.
