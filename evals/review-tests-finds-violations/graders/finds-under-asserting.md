---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Under-asserting` (or clearly
  equivalent category name) finding on `test_divide_works` in
  fixtures/test_calculator.py, for only checking that `divide(10, 2)` did
  not raise, without asserting the actual quotient (5.0) it returns.
  FAIL if no finding flags `test_divide_works`'s missing value assertion.
weight: 1
---

Reports `test_divide_works` checking only for "no exception" instead of the
actual quotient as an `Under-asserting` finding.
