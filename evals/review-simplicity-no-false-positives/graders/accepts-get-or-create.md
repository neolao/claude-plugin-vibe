---
type: llm
focus: last_message
criteria: |
  `get_or_create_cart` in fixtures/clean_ops.py does not merely forward to
  another function: it looks the cart up, builds a default when missing,
  stores it back, and records the new cart's id in `new_cart_ids` only when
  it created one — which `dict.setdefault` cannot express.

  PASS if no `high` or `medium` severity finding calls it a pointless
  wrapper, needless indirection, or a non-idiomatic `setdefault`.
  FAIL if it is flagged as Indirection or Non-idiomatic (or equivalent) at
  high or medium severity.
weight: 1
---

Does not call a get-or-create helper pointless indirection.
