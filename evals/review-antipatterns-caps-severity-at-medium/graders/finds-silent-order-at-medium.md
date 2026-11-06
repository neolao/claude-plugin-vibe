---
type: llm
focus: last_message
criteria: |
  `TaxCalculator` in fixtures/billing/tax.py must have `load_rates()`
  called before `total()`; nothing in the API expresses it, and
  fixtures/billing/invoice_export.py skips the call, so `total()` taxes
  at rate 0 without any error.

  PASS if the reported findings include a `Temporal coupling` (or clearly
  equivalent category name) finding on `TaxCalculator` / `load_rates` /
  `total` with SEVERITY `medium`.
  FAIL if no finding flags this required call order, or if that finding
  carries SEVERITY `high` or `low`.
weight: 2
---

Reports the silent call order at `medium`: a caller outside the unit gets
it wrong silently, which is the medium case; the wrong total it produces is
review-correctness' finding, not a reason for `high`.
