---
type: llm
focus: last_message
criteria: |
  `is_active` in fixtures/clean_ops.py returns early on `archived`, then on a
  missing `last_seen`, then compares `now - last_seen` to a window. Each
  return tests a different field, and two of them return computed
  expressions, not literals — it is not an if/else returning literal
  booleans, and folding the three returns into one `and`/`or` expression
  would read worse.

  PASS if no `high` or `medium` severity finding calls these guard clauses
  redundant or asks to fold them into a single boolean expression.
  FAIL if `is_active` is flagged as Redundant logic (or equivalent) at high
  or medium severity.
weight: 1
---

Does not call load-bearing guard clauses redundant.
