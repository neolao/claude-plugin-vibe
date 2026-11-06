---
type: llm
focus: last_message
criteria: |
  The scope is fixtures/promotions/. `apply_bundle` in
  fixtures/promotions/bundles.py calls `order.add_line(...)`, the method of
  the `Order` aggregate defined outside the scope in fixtures/orders/order.py
  that enforces the quantity rule, and reads nothing else of the order.
  `BUNDLES` is a module-level table of frozen `Bundle` values.

  PASS if no `high` or `medium` severity finding targets `apply_bundle`,
  `Bundle` or `BUNDLES` — for writing the aggregate's internals, for
  holding a rule that belongs on `Order`, for being anemic, or for the
  `Money(0, "EUR")` price of a bundled line. A report with no findings at
  all passes.
  FAIL if bundles.py is flagged for one of those reasons at high or medium
  severity, or if any finding is anchored outside fixtures/promotions/.
weight: 2
---

Does not flag a writer in scope that goes through the root's own method,
defined outside the path under review.
