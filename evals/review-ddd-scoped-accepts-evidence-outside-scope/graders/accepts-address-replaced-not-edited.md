---
type: llm
focus: last_message
criteria: |
  `Order.reroute` in fixtures/orders/order.py calls
  `self.shipping_address.with_street(street)` and assigns the result.
  `Address` (fixtures/customers/address.py) is a `@dataclass(frozen=True)`
  and `with_street` returns a new instance through `dataclasses.replace`,
  so the value object is replaced, never edited.

  PASS if no `high` or `medium` severity Value object finding claims
  `Address` is mutable, that `reroute` edits it in place, or that the
  customer's address changes with the order's. A report with no findings at
  all passes.
  FAIL if `reroute` or `Address` is flagged for one of those reasons at high
  or medium severity.
weight: 1
---

Does not call a value object mutated when its definition outside the path
under review is frozen and the method called returns a new instance.
