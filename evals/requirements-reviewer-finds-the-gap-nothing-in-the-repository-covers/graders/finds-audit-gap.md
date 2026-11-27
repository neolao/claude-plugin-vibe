---
type: llm
focus: last_message
criteria: |
  Criterion 3 asks each refusal to be recorded in the audit log with the
  coupon code. fixtures/audit.py offers `record(event, **fields)`, and
  nothing in the repository calls it: `apply_coupon` in
  fixtures/coupons.py raises `CouponError` without recording anything.

  PASS if a `(gap)` finding quotes criterion 3 (or its wording) and says
  the refusal is not recorded in the audit log, with a fix (call
  `audit.record` with the code before raising).
  FAIL if the missing audit record is not reported as a gap.
weight: 2
---

What nothing in the repository covers is a gap.
