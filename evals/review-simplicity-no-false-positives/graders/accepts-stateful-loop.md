---
type: llm
focus: last_message
criteria: |
  `merge_adjacent_discounts` in fixtures/clean_ops.py carries a running
  total across iterations, skips with `continue`, and flushes conditionally
  both inside and after the loop — control flow a comprehension cannot
  express.

  PASS if no `high` or `medium` severity finding says this loop should be a
  comprehension or calls it non-idiomatic.
  FAIL if it is flagged as Non-idiomatic (or equivalent) at high or medium
  severity.
weight: 1
---

Does not demand a comprehension for genuinely stateful control flow.
