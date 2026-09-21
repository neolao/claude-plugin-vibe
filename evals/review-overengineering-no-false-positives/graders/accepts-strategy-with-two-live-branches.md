---
type: llm
focus: last_message
criteria: |
  `PercentageDiscount` and `FixedAmountDiscount` are both selected at
  runtime in `price_order`, depending on the promo type.

  PASS if no `high` or `medium` severity Pattern without need finding
  targets the strategy.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not call a two-branch runtime strategy a pattern without need.
