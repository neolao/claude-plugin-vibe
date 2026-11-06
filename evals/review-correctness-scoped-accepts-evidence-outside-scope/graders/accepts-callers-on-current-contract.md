---
type: llm
focus: last_message
criteria: |
  `discount_rate(customer, today)` in fixtures/orders/pricing.py is called
  with two arguments by `checkout_total` in fixtures/orders/checkout.py
  and by `projected_discounts` in fixtures/reports/summary.py (outside
  the scope).

  PASS if no `high` or `medium` severity finding claims a caller of
  `discount_rate` passes the wrong number of arguments or is otherwise
  broken by its signature.
  FAIL if any caller is flagged as a Broken caller (or equivalent) at high
  or medium severity.
weight: 1
---

Does not flag a callee whose every caller, in and out of the scope,
matches its contract.
