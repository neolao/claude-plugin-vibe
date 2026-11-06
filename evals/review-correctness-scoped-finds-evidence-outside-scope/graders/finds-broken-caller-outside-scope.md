---
type: llm
focus: last_message
criteria: |
  `discount_rate(customer, today)` in fixtures/orders/pricing.py takes two
  parameters; `projected_discounts` in fixtures/reports/summary.py
  (outside the scope) calls `discount_rate(c)` with one argument, so the
  monthly report raises a `TypeError` as soon as it has one customer.
  fixtures/orders/checkout.py passes both arguments correctly.

  PASS if the reported findings include a `Broken caller` (or clearly
  equivalent category name) finding anchored on fixtures/orders/pricing.py
  that names the call in fixtures/reports/summary.py (or
  `projected_discounts`) as passing one argument to a two-argument
  function.
  FAIL if no finding names that caller, or if the finding is anchored on
  fixtures/reports/summary.py instead of the in-scope callee.
weight: 2
---

Reports the outside caller still on the old contract, anchored on the
in-scope callee: pricing.py alone shows a two-parameter function; only
reports/summary.py, outside the scope, shows a caller that breaks.
