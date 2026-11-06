---
type: llm
focus: last_message
criteria: |
  `reserve` in fixtures/stock/inventory.py reads the level, compares it
  with `qty`, then writes `available - qty` back, with no lock; the
  README and fixtures/api/app.py say the server is a
  `ThreadingHTTPServer`, one thread per request, and `/reserve` calls
  `reserve` directly.

  PASS if the reported findings include a `Race` (or clearly equivalent
  category name) finding on `reserve` describing two concurrent
  reservations that both pass the check and together take more than the
  stock holds (or overwrite each other's write), with SEVERITY `high` or
  `medium`.
  FAIL if no finding flags this check-then-act, or if it is rated `low`.
weight: 2
---

Reports the check-then-act on the shared stock dictionary: two clerks
reserving the last units at the same time both succeed.
