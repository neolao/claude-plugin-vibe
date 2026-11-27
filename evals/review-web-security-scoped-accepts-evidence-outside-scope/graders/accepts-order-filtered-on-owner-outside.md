---
type: llm
focus: last_message
criteria: |
  `order` in fixtures/portal/routes/account.py calls
  `orders.render(session["user_id"], order_id)`; `render` in
  fixtures/portal/orders.py, outside the scope, selects the order by id
  and `owner_id` together, so another visitor's id returns 404.

  PASS if no `high` or `medium` severity `Access control` (or clearly
  equivalent category name, such as IDOR) finding targets `order`. A `low`
  finding passes, and so does a report with no findings at all.
  FAIL if the order read is reported as reaching another visitor's order
  at high or medium severity.
weight: 1
---

Does not call an order read an IDOR when the renderer outside the scope
filters on the owner.
