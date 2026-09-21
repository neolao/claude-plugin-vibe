---
type: llm
focus: last_message
criteria: |
  `backfill_order_counts` in fixtures/migrate_price_history.py is an O(n*m)
  nested loop, but the module docstring states it is a one-shot migration
  run manually by an operator, outside the running server and off every
  request path — which this dimension's checklist excludes.

  PASS if no `high` or `medium` severity finding flags this nested loop.
  FAIL if it is flagged as Complexity (or equivalent) at high or medium
  severity.
weight: 1
---

Leaves a one-shot operator migration script out of scope.
