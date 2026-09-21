---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Aggregate` (or clearly equivalent
  category name, e.g. "Entity") finding on `fixtures/order.py`, for at least
  one of:
  - the `Order` class being an anemic data bag with no behaviour, its
    `items`/`status` mutated by free functions (`add_item`, `close_order`)
    instead of by methods on the aggregate, or
  - the line-item-count invariant (`len(order.items) > 50`) being enforced in
    the free function `close_order` instead of inside `Order` itself, so
    nothing stops other code from mutating `order.items` directly and
    bypassing it.
  Either one is enough to pass.
  FAIL if neither is flagged as an Aggregate/Entity issue.
weight: 2
---

Reports the anemic `Order` and/or its invariant enforced outside the class as
an Aggregate finding.
