---
type: llm
focus: last_message
criteria: |
  Both tests of fixtures/test_tokens.py pass today, but their verdict
  rests on `date.today()` inside `is_expired` (fixtures/tokens.py): the
  test with `date(2030, 1, 1)` starts failing on that day without any
  change to the code, and nothing in the test controls the date.

  PASS if an `Isolation` (or clearly equivalent category name, such as
  `Non-deterministic`, `Flaky` or `Wrong level`) finding names the
  dependence on the real clock / `date.today()` for one or both of these
  tests, anchored on fixtures/test_tokens.py or fixtures/tokens.py.
  FAIL if no finding mentions that these tests depend on the current
  date.
weight: 1
---

Reports the test whose result the real clock decides, although it is
green today.
