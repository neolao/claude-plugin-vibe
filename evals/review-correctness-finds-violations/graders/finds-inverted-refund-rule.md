---
type: llm
focus: last_message
criteria: |
  `can_refund` in fixtures/billing/refunds.py returns
  `order.status == "paid" or not order.shipped`; its docstring requires a
  paid order that has not shipped, so both conditions must hold.

  PASS if the reported findings include a `Wrong logic` (or clearly
  equivalent category name) finding on `can_refund` saying the `or` lets
  an order through that fails one of the two conditions (an unpaid order
  not yet shipped, or a paid order already shipped), with SEVERITY `high`
  or `medium`.
  FAIL if no finding flags this condition, or if it is rated `low`.
weight: 2
---

Reports the `or` that should be an `and`: an unpaid order that has not
shipped, or a paid order already on its way, gets a refund.
