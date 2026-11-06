---
type: llm
focus: last_message
criteria: |
  `export_invoice` in fixtures/api/handlers.py builds the export name as
  `f"invoice-{reference}-{date:%Y%m%d}.csv"`; `archive_exports` in
  fixtures/jobs/archive.py, outside the scope, takes it apart with
  `name[:-4].split("-")` into three parts and slices the date stamp. The
  format is defined at each end and nothing round-trips it.

  PASS if the reported findings include a finding anchored (its FILE: line)
  on fixtures/api/handlers.py, in category `Producer/reader format` (or a
  clearly equivalent name), whose ISSUE or SUGGESTION names
  fixtures/jobs/archive.py (or `archive_exports` / the `split("-")`) as
  the reader.
  FAIL if no finding names the filename format, or if the finding never
  points at the reader in fixtures/jobs/archive.py.
weight: 2
---

Reports the producer/reader format with the outside reader as evidence,
anchored on the producer in scope.
