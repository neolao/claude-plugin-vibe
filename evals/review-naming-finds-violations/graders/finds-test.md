---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Test` (or clearly equivalent
  category name) finding on `test_calc` in
  fixtures/test_order_processor.py, for naming the test after the method
  under test (`calc`) instead of the behaviour and expected outcome (e.g. it
  applies a promo discount to the total).
  FAIL if no finding flags `test_calc`'s name for this reason.
weight: 1
---

Reports `test_calc` describing the method under test rather than the
behaviour/outcome as a `Test` finding.
