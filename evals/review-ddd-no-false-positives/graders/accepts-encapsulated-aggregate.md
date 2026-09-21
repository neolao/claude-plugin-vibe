---
type: llm
focus: last_message
criteria: |
  `Order` in fixtures/order.py enforces its own invariants (max line items,
  no closing an empty order) in `add_item`/`close`, keeps `_items`/`_status`
  private, and exposes items only as a read-only tuple.

  PASS if no `high` or `medium` severity Aggregate or Entity finding claims
  its invariants are enforced outside the class or that it is an anemic
  data bag.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not call a self-enforcing aggregate root anemic.
