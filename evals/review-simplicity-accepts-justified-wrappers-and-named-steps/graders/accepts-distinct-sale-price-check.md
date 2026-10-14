---
type: llm
focus: last_message
criteria: |
  `effective_price` in fixtures/billing.py checks that a sale price exists
  and that it is below the regular price, then returns one of the two. The
  two parts of the condition test different things.

  PASS if no finding reports `effective_price` as `Redundant logic`,
  `Non-idiomatic` or `Complexity`, or asks to rewrite or fold it.
  FAIL if such a finding targets `effective_price`.
weight: 1
---

Does not flag a condition whose two operands test different facts.
