---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Decision violated` (or clearly
  equivalent category name) finding citing
  `.vibe/decisions/002-no-raw-sql-in-core.md` (by id, by title, or by
  clearly describing its content) against `monthly_totals` in
  `fixtures/core/reporting.py`, which opens its own `psycopg2` connection
  and runs a raw `SELECT` — exactly what that decision forbids `core/` from
  doing.
  FAIL if no finding references this decision as violated by
  `core/reporting.py`.
weight: 1
---

Reports `core/reporting.py`'s raw SQL against the recorded no-raw-SQL-in-core
decision as a `Decision violated` finding.
