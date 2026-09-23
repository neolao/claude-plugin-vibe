---
type: llm
focus: last_message
criteria: |
  `OrderController` → `OrderPricingService` → `OrderRepository` in
  fixtures/order_pricing.py gives each layer distinct work: the controller
  validates the request and maps missing or malformed ids to 400/404, the
  service applies the discount, shipping and tax rules, and the repository
  runs the SQL query and maps the row to typed values.

  PASS if no `high` or `medium` severity Disproportionate structure or
  Pattern without need finding targets this split or one of its three
  classes.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not call a three-way split with real work in each layer disproportionate.
