---
type: llm
focus: last_message
criteria: |
  `get_or_create_cart` in fixtures/clean_ops.py does not merely forward to
  another function: it looks the cart up, builds a default when missing, and
  stores it back.

  PASS if no `high` or `medium` severity finding calls it a pointless
  wrapper or needless indirection.
  FAIL if it is flagged as Indirection (or equivalent) at high or medium
  severity.
weight: 1
---

Does not call a get-or-create helper pointless indirection.
