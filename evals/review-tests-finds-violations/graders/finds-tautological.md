---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Tautological` (or clearly
  equivalent category name) finding, rated high severity, on `test_add` in
  fixtures/test_calculator.py — the expected value (`a + b`) is computed
  with the exact same logic/formula as the `add()` implementation under
  test, so a subtly wrong implementation could still pass.
  FAIL if `test_add` is not flagged as tautological, or if a genuinely
  tautological test is rated low/medium instead of high.
weight: 2
---

Reports `test_add`'s self-referential expected-value computation as a
high-severity `Tautological` finding.
