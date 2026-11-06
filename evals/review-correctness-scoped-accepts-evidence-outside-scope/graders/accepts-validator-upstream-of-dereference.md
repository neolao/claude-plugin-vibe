---
type: llm
focus: last_message
criteria: |
  `receipt_recipient` in fixtures/orders/receipt.py reads `.email` on the
  result of `customers.get(order.customer_id)`. Its only caller path is
  `build_receipt`, called from the `/receipt` handler in
  fixtures/app/server.py (outside the scope), which answers 404 and
  returns when the order is missing or `order.customer_id not in
  customers`.

  PASS if no `high` or `medium` severity finding claims `receipt_recipient`
  (or `build_receipt`) dereferences `None` or crashes on a removed
  customer.
  FAIL if it is flagged as a Null/absent issue (or equivalent) at high or
  medium severity.
weight: 1
---

Does not flag a dereference a validator on the only reaching path already
excludes: the handler, outside the scope, checks the customer before
calling.
