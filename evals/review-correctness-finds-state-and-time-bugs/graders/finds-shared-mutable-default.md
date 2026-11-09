---
type: llm
focus: last_message
criteria: |
  `enqueue` in fixtures/jobs/queue.py declares `pending=[]` and
  `schedule_nightly` in fixtures/jobs/runner.py calls it twice without a
  list, so both calls append to the same default list: the invoice task
  and the export task end up in one list, and `drain` hands both out
  twice-mixed (the first `drain` returns both tasks and empties the list).

  PASS if the findings include one on `enqueue` or `schedule_nightly`
  (any category such as Wrong logic or Broken caller) saying the default
  list is shared between calls, with SEVERITY `high` or `medium`.
  FAIL if no finding reports the shared default list, or it is rated `low`.
weight: 2
---

Reports the mutable default argument whose state leaks between calls.
