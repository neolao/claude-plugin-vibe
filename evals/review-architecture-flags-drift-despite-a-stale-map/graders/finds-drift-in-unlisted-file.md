---
type: llm
focus: last_message
criteria: |
  fixtures/core/discounts.py is not in the `Files:` list of
  `.vibe/modules/core.md` (the map predates it), yet it imports `psycopg2`
  and `adapters.config` and runs a `SELECT` inside a zone whose role is
  "pure business/domain logic ... no I/O, no framework, database, or mail
  imports" and whose `Depends on` is "(none — the innermost layer)". A
  sync would list the file and record the import; it would not make either
  fit the role.

  PASS if the reported findings include a `Layer direction` or a `Module
  scope` (or clearly equivalent category name) finding anchored on
  fixtures/core/discounts.py (or on the `core` module because of it), for
  the driver import, the `adapters.config` import, or the SQL inside core.
  FAIL if no finding flags fixtures/core/discounts.py.
weight: 2
---

Reports the drift of a file the stale map does not list: the map's omission
is not a pass.
