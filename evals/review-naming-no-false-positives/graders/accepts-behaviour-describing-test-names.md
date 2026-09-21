---
type: llm
focus: last_message
criteria: |
  `test_calculate_discounted_total_applies_promo_discount` and
  `test_is_active_returns_false_when_order_missing` each name the behaviour
  and its outcome; that they also contain the method under test is normal.

  PASS if no `high` or `medium` severity Test finding says either name
  describes the method instead of the behaviour, or should drop the method
  name.
  FAIL if either is flagged at high or medium severity.
weight: 1
---

Does not penalise a test name for also naming the method it covers.
