---
type: llm
focus: last_message
criteria: |
  `order` in fixtures/portal/routes/account.py returns
  `orders.render(order_id)` for any id in the URL; `render` in
  fixtures/portal/orders.py, outside the scope, selects the order by id
  alone and never compares its `owner_id` to the signed-in visitor, so any
  account reads any other visitor's order and address by swapping the id.

  PASS if the reported findings include an `Access control` (or clearly
  equivalent category name, such as IDOR) finding whose FILE: line points
  to fixtures/portal/routes/account.py, that names the missing owner check
  on the order, and whose ISSUE or SUGGESTION names `orders.render`,
  fixtures/portal/orders.py or the query by id alone. A finding that calls
  this route unauthenticated does not count: the login hook covers
  `/account/`.
  FAIL if no finding reports the order read, or if the finding is anchored
  (its FILE: line) on fixtures/portal/orders.py.
weight: 1
---

Judges what the guarded route does with the account it has: the outside
renderer shows the owner is never checked.
