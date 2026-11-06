---
type: llm
focus: last_message
criteria: |
  `Money` in fixtures/pricing/money.py is a plain class compared by value
  whose operations return new instances. `apply_loyalty_discount` in
  fixtures/discounts/apply.py writes `line.unit_price.cents` in place; that
  `Money` is the catalog product's `price` (fixtures/catalog/product.py),
  handed to the line by `place_order` in fixtures/checkout/basket.py, so
  the discount also changes the catalog price every later basket reads.

  PASS if the reported findings include a `Value object` (or clearly
  equivalent category name) finding anchored on fixtures/discounts/apply.py
  or fixtures/pricing/money.py whose ISSUE names the in-place write in
  `apply_loyalty_discount` (not merely that `Money` lacks `frozen` or a
  record type).
  FAIL if no finding flags the write, or if the only Value object finding
  blames `Money`'s definition without naming a write that happens.
weight: 2
---

Reports the write that happens on a shared value, not the language's
inability to enforce immutability.
