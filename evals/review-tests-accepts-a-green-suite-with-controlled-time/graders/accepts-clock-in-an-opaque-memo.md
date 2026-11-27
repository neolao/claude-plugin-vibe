---
type: llm
focus: last_message
criteria: |
  `test_balance_sums_posted_amounts` in fixtures/test_ledger.py reads
  `date.today()` only to build the memo strings it posts; its assertion
  is on `balance()`, which sums the amounts and never reads a memo. The
  verdict is `6` on any day.

  PASS if no `high` or `medium` severity `Isolation` (or clearly
  equivalent category name) finding claims this test's result depends on
  the clock. A `low` finding passes, and so does a report with no
  findings at all.
  FAIL if this test is reported at high or medium severity as
  clock-dependent.
weight: 1
---

A clock read that cannot change the asserted value is not Isolation: the
rule is about what the result depends on, not what the test touches.
