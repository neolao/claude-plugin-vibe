---
type: llm
focus: last_message
criteria: |
  Criterion 1 is met: `apply_coupon` raises `CouponError("Coupon expired")`
  when the coupon's expiry date is before today. `CouponError`, the
  optional `today` parameter and the tests serve the request.

  PASS if no `(gap)` finding targets criterion 1, and no `(addition)`
  finding targets `CouponError`, the `today` parameter, or the test file.
  FAIL if any of those is reported.
weight: 1
---

A met criterion and the machinery that serves it are not findings.
