---
type: llm
focus: last_message
criteria: |
  The fixtures use only idiomatic/clean naming: `OrderRepository` (a legitimate
  architectural role, not a vague `Manager`/`Helper`/`Utils`/`Service` suffix),
  a boolean method already phrased as a question (`is_active`), a single-letter
  `e` parameter for an event in `EventBus.publish` (the checklist's own example
  of an idiomatic short name), consistent snake_case file names across the
  directory, and test names that already describe behaviour and outcome
  (`test_calculate_discounted_total_applies_promo_discount`,
  `test_is_active_returns_false_when_order_missing`).

  PASS if the response reports no `high` or `medium` severity Variable,
  Function, Type, Module, or Test finding on this code — either no findings at
  all, or only `low` severity style notes unrelated to these already-clean
  patterns.
  FAIL if it flags `OrderRepository`'s suffix as vague, `is_active` as not
  phrased as a question, the `e` parameter as cryptic, the file naming as
  inconsistent, or either test name as describing the method instead of the
  behaviour.
weight: 2
---

Does not invent naming findings on code that already follows the idiomatic
pattern for each category.
