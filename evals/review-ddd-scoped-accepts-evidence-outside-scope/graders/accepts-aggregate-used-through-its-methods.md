---
type: llm
focus: last_message
criteria: |
  `Order` in fixtures/orders/order.py keeps `_lines` private, enforces the
  1..10 quantity rule in `add_line` and exposes `lines` as a tuple. Nothing
  in the scope writes to it, and outside the scope `apply_bundle`
  (fixtures/promotions/bundles.py) and `PlaceOrder`
  (fixtures/checkout/place_order.py) add lines through `add_line`, while
  `quote` (fixtures/shipping/quote.py) only iterates `order.lines`.

  PASS if no `high` or `medium` severity Aggregate (or Entity) finding
  claims `Order`'s internals are written from outside, that its quantity
  rule is bypassed, that it is an anemic data bag, or that `quote` breaches
  it by reading `lines`. A report with no findings at all passes.
  FAIL if `Order` is flagged for one of those reasons at high or medium
  severity.
weight: 1
---

Does not call an aggregate breached when every writer outside the path under
review goes through its methods and the only other use is a read of its
read-only view.
