---
type: llm
focus: last_message
criteria: |
  `PRIORITIES = ("low", "normal", "urgent")` in fixtures/tickets/priority.py
  is copied as `const PRIORITIES = ["low", "normal", "urgent"]` in
  fixtures/web/static/priority.js. fixtures/tests/test_priority.py asserts
  `set(SLA_HOURS) == set(PRIORITIES)` — a check between the backend list
  and the backend table that never reads the JavaScript copy.

  PASS if the reported findings include a `Duplicated case list` (or
  clearly equivalent category name) finding that names both
  fixtures/tickets/priority.py and fixtures/web/static/priority.js with
  SEVERITY `medium` (or `high`).
  FAIL if no finding names the two copies of the priority list, if the
  finding is rated `low`, or if it treats the backend test as a guard of
  the JavaScript copy.
weight: 2
---

Reports the cross-tier copy at `medium` despite the backend-only test: a
guard counts only when it reaches both expressions, and this one reaches
the Python list and its SLA table, never the browser's copy.
