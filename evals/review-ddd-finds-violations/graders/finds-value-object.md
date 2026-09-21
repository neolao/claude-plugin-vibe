---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Value object` (or clearly
  equivalent category name) finding on the `Money` class in
  fixtures/money.py, for at least one of: `add` mutating `self.amount` in
  place instead of returning a new `Money` (Value objects should be
  immutable), or `Money` having no `__eq__`/value-based equality so two
  instances with the same amount and currency are not equal.
  FAIL if no finding flags `Money` for either reason.
weight: 1
---

Reports `Money`'s mutability or missing value-equality as a Value object
finding.
