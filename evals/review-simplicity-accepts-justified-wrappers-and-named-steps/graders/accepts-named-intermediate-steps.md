---
type: llm
focus: last_message
criteria: |
  `compute_invoice_line` in fixtures/billing.py names each intermediate
  value (`unit_price`, `net`, `tax`, `gross`) and logs each at debug level.

  PASS if no finding asks to inline those variables, collapse the function
  into one expression, or reports the function as `Indirection`, `Length` or
  `Redundant logic`.
  FAIL if such a finding targets `compute_invoice_line`.
weight: 1
---

Does not flag deliberately named intermediate steps that are logged.
