---
type: llm
focus: last_message
criteria: |
  `receipt_recipient` in fixtures/billing/notify.py reads `.email` on the
  result of `customers.get(order.customer_id)`. Its only caller path is
  `build_receipt`, called from the `/payments` handler in
  fixtures/api/app.py, which answers 404 and returns when the order is
  missing or `order.customer_id not in customers` — the `get` cannot miss
  on the path that reaches it.

  PASS if no `high` or `medium` severity finding claims `receipt_recipient`
  (or `build_receipt`) dereferences `None` or crashes on a removed customer.
  FAIL if it is flagged as a Null/absent issue (or equivalent) at high or
  medium severity.
weight: 1
---

Does not flag a dereference a validator on every reaching path already
excludes: the handler checks the customer before calling.
