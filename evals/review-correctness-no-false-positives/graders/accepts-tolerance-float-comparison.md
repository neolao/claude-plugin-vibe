---
type: llm
focus: last_message
criteria: |
  `is_settled` in fixtures/billing/settlement.py compares the float sum
  of the payments with the invoice total through `math.isclose(...,
  abs_tol=HALF_CENT)`, as its docstring says ("to the cent").

  PASS if no `high` or `medium` severity finding claims `is_settled`
  compares floats exactly, misses a fully paid invoice through a rounding
  error, or that its tolerance is wrong.
  FAIL if it is flagged as a Numbers/time (or float-precision) issue at
  high or medium severity.
weight: 1
---

Does not flag a float comparison done with a tolerance.
