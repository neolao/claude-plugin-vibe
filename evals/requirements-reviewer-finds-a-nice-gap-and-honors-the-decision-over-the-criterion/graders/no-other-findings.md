---
type: llm
focus: last_message
criteria: |
  Criterion 2 (the archive runs every night) is met by `register` in
  fixtures/archive.py, which hands `archive_old` to `every_night(2, …)`
  of fixtures/scheduler.py; criterion 3 (a one-line summary with the
  number of rows moved) by the `log.info("archived %d transactions", …)`
  line. `Ledger`, `months_between` and the tests serve the request.

  PASS if no `(gap)` finding targets criterion 2 or 3, and no `(addition)`
  finding targets `Ledger`, `months_between`, `register`, the scheduler
  registration, or the test file.
  FAIL if any of those is reported.
weight: 1
---

Met criteria and the machinery that serves them are not findings.
