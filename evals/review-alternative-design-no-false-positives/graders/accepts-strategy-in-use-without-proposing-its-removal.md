---
type: llm
focus: last_message
criteria: |
  `DiscountStrategy` in fixtures/pricing/discounts.py has two
  implementations, both selected at checkout by `price_order`. Whether
  that machinery is worth keeping is `review-overengineering`'s question;
  the alternative-design agent proposes only a named design that wins,
  never the removal of one.

  PASS if no `high` or `medium` severity finding proposes replacing
  `DiscountStrategy` and its two subclasses with plain functions, a single
  conditional or "just inline it". A finding that proposes a different
  named design for the discounts (for example a registry keyed by promo
  type) does not fail this grader. A report with no findings at all
  passes.
  FAIL if the agent proposes, at high or medium severity, to collapse the
  strategy into conditionals or plain functions.
weight: 1
---

Does not take `review-overengineering`'s axis: removing machinery is not an
alternative design.
