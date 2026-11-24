---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Lost context` (or clearly
  equivalent category name) finding on `refund_order`
  (fixtures/billing/refunds.py) for the error it raises through
  `billing_error(result)`: `billing_error` (fixtures/common/errors.py)
  returns `BillingError("refund failed")` and drops the provider's `code`
  and the `payment_id` that `RefundResult` carries, so a declined card, an
  already-refunded payment and a provider limit all reach the support
  console as the same message with no identifier.
  FAIL if no finding flags this generic error.
weight: 1
---

Reports the refund failure collapsed into one message without its code or
payment id. refunds.py alone shows a dedicated error builder; only
common/errors.py, outside the scope, shows it ignores its argument.
