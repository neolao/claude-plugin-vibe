---
type: llm
focus: last_message
criteria: |
  `is_active` in fixtures/clean_ops.py short-circuits on `archived`, a
  different field from the `status` the return expression tests, so the
  guard cannot be folded into that expression — it is not an if/else both
  returning a literal boolean.

  PASS if no `high` or `medium` severity finding calls this guard redundant.
  FAIL if it is flagged as Redundant logic (or equivalent) at high or medium
  severity.
weight: 1
---

Does not call a load-bearing guard clause redundant.
