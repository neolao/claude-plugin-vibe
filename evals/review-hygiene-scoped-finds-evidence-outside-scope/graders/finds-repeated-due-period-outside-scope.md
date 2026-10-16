---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Duplication` (or clearly
  equivalent category name) finding on the 30-day payment term
  (`timedelta(days=30)`) in fixtures/billing/invoices.py that names at least
  one of its other copies outside the scope, fixtures/reminders/overdue.py
  or fixtures/reports/aging.py, and suggests one named constant or one
  shared helper.
  FAIL if no finding flags the repeated 30-day term, or if the finding names
  no file outside fixtures/billing/.
weight: 1
---

Reports the `timedelta(days=30)` payment term in fixtures/billing/invoices.py
as a `Duplication` finding (a magic value deserving one named constant) and
names a copy in fixtures/reminders/ or fixtures/reports/. Inside the scope the
value appears once: the repetition is only visible to an agent that greps the
whole repository.
