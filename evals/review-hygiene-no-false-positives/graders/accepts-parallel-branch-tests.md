---
type: llm
focus: last_message
criteria: |
  `test_calculate_discounted_total_applies_promo` and
  `test_calculate_discounted_total_without_promo` in
  fixtures/test_order_repository.py share an arrange-act-assert shape but
  each drives a different branch (promo / no promo) with different inputs
  and a different expected value.

  PASS if no `high` or `medium` severity finding calls these two tests
  copy-pasted or duplicated.
  FAIL if they are flagged as Duplication (or equivalent) at high or medium
  severity.
weight: 1
---

Does not call two branch-per-test cases copy-paste duplication.
