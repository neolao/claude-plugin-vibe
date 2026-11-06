---
type: llm
focus: last_message
criteria: |
  `is_overdue` in fixtures/tickets/model.py returns `ticket.status ==
  "open" and ticket.due_at < now`; `overdue_tickets` in
  fixtures/reports/overdue.py filters with the same `t.status == "open"
  and t.due_at < now` written again instead of calling `is_overdue`.
  Nothing tests that the two agree.

  PASS if the reported findings include a `Restated rule` (or clearly
  equivalent category name) finding that names both
  fixtures/tickets/model.py and fixtures/reports/overdue.py (or
  `is_overdue` and `overdue_tickets`) and suggests the report call the
  model's rule.
  FAIL if no finding names the two expressions of the overdue rule.
weight: 2
---

Reports the predicate rewritten in the report with the same fields and
condition as the model's function, naming which side should hold the
single definition.
