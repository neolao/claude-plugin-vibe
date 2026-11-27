---
type: llm
focus: last_message
criteria: |
  Both tests of fixtures/test_tokens.py pass the day explicitly
  (`today=date(2029, 12, 31)`, `today=date(2030, 1, 2)`) to
  `is_expired`, which reads no clock of its own: their verdict is the
  same on any day the suite runs.

  PASS if no `high` or `medium` severity `Isolation` (or clearly
  equivalent category name, such as `Non-deterministic`, `Flaky` or
  `Wrong level`) finding claims these tests depend on the current date
  or the real clock. A `low` finding passes, and so does a report with
  no findings at all.
  FAIL if either test is reported at high or medium severity as
  depending on the real clock.
weight: 1
---

Does not call a test clock-dependent when the day is an explicit input.
