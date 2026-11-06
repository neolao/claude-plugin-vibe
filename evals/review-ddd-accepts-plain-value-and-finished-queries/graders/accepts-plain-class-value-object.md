---
type: llm
focus: last_message
criteria: |
  `Money` in fixtures/pricing/money.py is a plain class — no `frozen`, no
  record — with no setter, operations that return a new instance,
  `__eq__` and `__hash__` by value. Nothing in the repository writes
  `cents` or `currency` after construction: `Order.apply_discount` in
  fixtures/orders/order.py rebuilds its lines with new `Money` values and
  fixtures/discounts/apply.py calls that method.

  PASS if no `high` or `medium` severity Value object finding claims
  `Money` is mutable, should be frozen or a record, or is edited in place.
  A report with no findings at all passes.
  FAIL if `Money` is flagged for one of those reasons at high or medium
  severity.
weight: 2
---

Does not call a value object mutable for what the language cannot enforce
when the project treats it as a value and nothing writes it.
