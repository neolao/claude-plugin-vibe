---
type: llm
focus: last_message
criteria: |
  `test_memos_keep_posting_order` in fixtures/test_ledger.py calls
  `ledger.post(value=10, memo="rent")`; `Ledger.post` in
  fixtures/ledger.py takes `(amount, memo)`, as fixtures/README.md
  documents and as `test_balance_sums_posted_amounts` calls it, so the
  run raises `TypeError: unexpected keyword argument 'value'`. The test
  is stale and the code is right.

  PASS if a `Failing test` (or clearly equivalent category name) finding
  is anchored (its FILE: line) on fixtures/test_ledger.py and its ISSUE
  says the test is wrong — the keyword `value` does not exist, the call
  must pass `amount` — not the code.
  FAIL if no finding reports this error, or if the finding says
  `Ledger.post` should accept `value` or is otherwise the wrong side.
weight: 2
---

Reports the stale call as a Failing test on the test, and says the test,
not the code, is the wrong side.
