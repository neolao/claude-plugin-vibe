---
type: llm
focus: last_message
criteria: |
  `OrderController` → `OrderPricingService` → `OrderRepository` separates
  request handling, multi-rule pricing (tax, discount, shipping) and
  persistence, each doing distinct work.

  PASS if no `high` or `medium` severity Disproportionate structure finding
  targets this split.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not call a three-way split with real work in each layer disproportionate.
