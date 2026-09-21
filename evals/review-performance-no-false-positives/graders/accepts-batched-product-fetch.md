---
type: llm
focus: last_message
criteria: |
  `checkout` in fixtures/checkout_handler.py collects the product ids first
  and resolves them in a single `db.get_products_by_ids(...)` call before
  the loop; the loop itself only does arithmetic over data already fetched.

  PASS if no `high` or `medium` severity finding calls this an N+1 query
  pattern.
  FAIL if it is flagged as N+1 (or equivalent) at high or medium severity.
weight: 1
---

Does not call a pre-batched fetch an N+1.
