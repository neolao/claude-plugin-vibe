---
type: llm
focus: last_message
criteria: |
  `is_settled` in fixtures/billing/settlement.py compares
  `sum(p.amount for p in payments) == invoice.total` where amounts and
  totals are floats parsed from the provider's JSON (the module docstring
  and fixtures/billing/model.py say so).

  PASS if the reported findings include a `Numbers/time` (or clearly
  equivalent category name, such as a float-equality or precision
  finding) on `is_settled` saying that the float sum can differ from the
  total by a rounding error (e.g. 0.1 + 0.2 != 0.3), so a fully paid
  invoice is reported unsettled, with SEVERITY `high` or `medium`.
  FAIL if no finding flags this float equality, or if it is rated `low`.
weight: 2
---

Reports the exact equality between floats produced by arithmetic: an
invoice paid in several instalments can stay unsettled forever.
