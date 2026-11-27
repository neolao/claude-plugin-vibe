---
type: llm
focus: last_message
criteria: |
  `order` in fixtures/app.py sits behind `login_required` and selects the
  order by id and `owner_id = session["user_id"]` together, so another
  customer's id returns 404.

  PASS if no `high` or `medium` severity `Access control` (or clearly
  equivalent category name, such as IDOR) finding targets `order`. A
  `low` finding passes, and so does a report with no findings at all.
  FAIL if the order read is reported as reaching another customer's
  order at high or medium severity.
weight: 1
---

Does not call an owner-filtered read an IDOR.
