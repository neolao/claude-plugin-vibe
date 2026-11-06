---
type: llm
focus: last_message
criteria: |
  fixtures/web/cart_view.py imports `FREE_SHIPPING_THRESHOLD` from
  fixtures/pricing/fees.py and uses it in `shipping_banner`; the value
  `50.0` is written once, in fees.py.

  PASS if no `high` or `medium` severity finding names the free-shipping
  threshold, `FREE_SHIPPING_THRESHOLD` or `shipping_banner` as a copied
  constant, a restated rule or any coordination to maintain. A report
  with no findings at all passes.
  FAIL if the threshold is flagged at high or medium severity.
weight: 1
---

Does not report a value that both sites reach through one shared
definition: there is only one expression of it.
