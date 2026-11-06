---
type: llm
focus: last_message
criteria: |
  `discount_rate(customer, today)` in fixtures/billing/pricing.py takes
  two parameters. `projected_discounts` in fixtures/reports/summary.py
  calls `discount_rate(c)` with one argument, so the monthly report
  raises a `TypeError` as soon as it has one customer;
  fixtures/billing/checkout.py passes both arguments correctly.

  PASS if the reported findings include a `Broken caller` (or clearly
  equivalent category name) finding that names the call in
  fixtures/reports/summary.py (anchored there or on
  fixtures/billing/pricing.py naming it) as passing one argument to a
  two-argument function, with SEVERITY `high` or `medium`.
  FAIL if no finding flags this call, if it flags
  fixtures/billing/checkout.py as broken, or if it is rated `low`.
weight: 2
---

Reports the one caller still on the one-argument contract, found by
grepping the callers of `discount_rate` outside `billing/`.
