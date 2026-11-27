---
type: llm
focus: last_message
criteria: |
  fixtures/docs/architecture.md says the OFX reader is
  `src/parsers/ofx.py`; no such file exists — the reader is
  fixtures/src/parsers/ofx_reader.py. The CSV reader it cites,
  `src/parsers/csv_reader.py`, exists.

  PASS if the reported findings include a `Dangling reference` (or
  clearly equivalent category name) finding whose FILE: line points to
  fixtures/docs/architecture.md and that names `src/parsers/ofx.py` as
  the path that resolves nowhere (naming `ofx_reader.py` as the fix is a
  bonus, not required).
  FAIL if no finding reports that cited path, or if a finding reports
  `src/parsers/csv_reader.py`, `src/reconcile.py` or `src/export.py` as
  missing.
weight: 2
---

Reports the backticked path a doc presents as the module's location when
nothing sits there, and leaves the three paths that resolve alone.
