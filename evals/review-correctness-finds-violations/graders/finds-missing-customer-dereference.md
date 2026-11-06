---
type: llm
focus: last_message
criteria: |
  `receipt_recipient` in fixtures/billing/notify.py does
  `customers.get(order.customer_id)` then reads `.email` on the result
  with no check. fixtures/billing/model.py states that a customer account
  can be removed from the directory while its orders are kept, and the
  payment handler in fixtures/api/app.py calls `build_receipt` for any
  invoice's order.

  PASS if the reported findings include a `Null/absent` (or clearly
  equivalent category name) finding on `receipt_recipient` saying the
  `get` returns `None` for a removed customer and the `.email` access
  then raises, with SEVERITY `high` or `medium`.
  FAIL if no finding flags this dereference, or if it is rated `low`.
weight: 2
---

Reports the `.email` read on a `get` that misses: a payment recorded on an
order whose customer was removed crashes the payment handler.
