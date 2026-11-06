---
type: llm
focus: last_message
criteria: |
  `STATUS_LABELS` in fixtures/reports/export.py and `STATUSES` in
  fixtures/orders/status.py carry the same four statuses, and
  fixtures/tests/test_export.py asserts `set(STATUS_LABELS) ==
  set(STATUSES)`, so adding or removing a status on either side fails the
  suite.

  PASS if no `high` or `medium` severity finding names `STATUS_LABELS`,
  `STATUSES` or the status list as a duplicated case list, a parallel
  table or any coordination to maintain. A report with no findings at all
  passes.
  FAIL if the status list is flagged at high or medium severity.
weight: 1
---

Does not report two lists that a test keeps aligned: a test that compares
both sides is a real guard.
