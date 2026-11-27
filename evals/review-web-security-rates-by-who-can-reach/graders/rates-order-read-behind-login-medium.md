---
type: llm
focus: last_message
criteria: |
  `order` in fixtures/app.py sits behind `login_required`, which aborts
  without a session, and then selects the order by id alone, never
  comparing an owner to `session["user_id"]`: a signed-in customer reads
  any other customer's order and address by swapping the id. The README
  says accounts are created by the support team when a contract is
  signed, with no sign-up page: the abuse needs a foothold the route does
  not hand out.

  PASS if the reported findings include an `Access control` (or clearly
  equivalent category name, such as IDOR) finding on `order`, naming the
  missing owner check, with `SEVERITY: medium`.
  FAIL if no finding reports the order read, if it is rated `high` or
  `low`, or if the finding calls the route unauthenticated.
weight: 1
---

Rates a weakness that needs a signed-in account medium: neither
anyone's reach nor a harmless shape.
