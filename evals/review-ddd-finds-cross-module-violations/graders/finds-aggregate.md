---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Aggregate` (or clearly equivalent
  category name, e.g. "Entity") finding for `apply_bundle` in
  fixtures/shop/promotions.py appending straight to `cart._lines`, which
  writes the `Cart` aggregate's internals from outside and skips
  `Cart.add_line`'s 1..`MAX_QTY_PER_LINE` (10) quantity check — the
  `SUMMER` bundle adds 12. The finding may be anchored on promotions.py or
  on cart.py, as long as it names this write from promotions.py.
  FAIL if no finding flags this bypass of the aggregate.
weight: 1
---

Reports the promotion module writing `Cart._lines` directly, around the
aggregate's quantity invariant, as an Aggregate finding.
