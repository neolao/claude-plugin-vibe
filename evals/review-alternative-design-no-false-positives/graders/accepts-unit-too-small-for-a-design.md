---
type: llm
focus: last_message
criteria: |
  `round_to_cents` in fixtures/pricing/rounding.py is a four-line helper
  over `Decimal.quantize`, and fixtures/pricing/test_rounding.py is its
  unit test.

  PASS if no finding of any severity proposes an alternative design for
  `round_to_cents` or for the test file (a value object for money, a
  rounding strategy, a pipeline, or anything else). A report with no
  findings at all passes.
  FAIL if any finding targets fixtures/pricing/rounding.py or
  fixtures/pricing/test_rounding.py.
weight: 1
---

Stays silent on a unit too small to carry a design.
