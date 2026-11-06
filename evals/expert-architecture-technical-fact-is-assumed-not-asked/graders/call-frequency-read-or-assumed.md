---
type: llm
focus: last_message
criteria: |
  The fixture answers how hot `total()` is: `shop/checkout.py` calls it
  once when the customer pays, `shop/cart_view.py` on every cart page load
  and quantity change, over a handful of lines each time. The expert's
  rule: a technical fact it could not establish is read from the code, or
  stated as an assumption with the option that holds if it is wrong —
  never asked. Its grid also requires saying whether the runtime-cost
  criterion is decisive here (hot path) or negligible.

  PASS if the reply settles the call frequency itself: by citing the
  callers (checkout once per order, the cart view per page load or
  change) or by stating an explicit assumption about it together with
  what would change if the assumption is wrong — and says whether runtime
  cost is decisive or negligible for this choice.
  FAIL if the reply asks the caller or the Product Owner how hot the
  pricing code is or how often it runs, or leaves the recommendation
  hanging on that fact without an assumption.
weight: 2
---

Settles the hot-path question from the fixture's callers or an explicit
assumption, instead of asking it.
