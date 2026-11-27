---
type: llm
focus: last_message
criteria: |
  `test_net_pay_rounding` in fixtures/test_payroll.py is skipped with the
  reason "duplicate of test_net_pay_rounds_to_the_cent, tracked in
  #214"; `test_net_pay_rounds_to_the_cent` is active and asserts the
  same call and the same literal. The rounding case is verified by the
  run.

  PASS if no `high` or `medium` severity `Dead test code` (or clearly
  equivalent category name, such as `Missing negative cases` or
  `Coverage gap`) finding targets the skipped test or claims the
  rounding case is unverified. A `low` finding passes, and so does a
  report with no findings at all.
  FAIL if the skipped duplicate is reported at high or medium severity,
  or if any finding says the rounding of `net_pay` has no active test.
weight: 2
---

A skipped duplicate whose reason names the active test and a tracked
issue leaves the case verified: low at most.
