---
type: llm
focus: last_message
criteria: |
  `export_invoice` in fixtures/api/handlers.py names the export through
  `invoice_filename` of fixtures/core/filenames.py, and `archive_exports`
  in fixtures/jobs/archive.py reads it back through
  `parse_invoice_filename` of the same module; fixtures/tests/test_filenames.py
  round-trips the two. The format is written in one place.

  PASS if no `high` or `medium` severity finding names the export filename,
  `invoice_filename`, `export_invoice` or the archive job as a
  producer/reader format or any coordination to maintain. A `low` finding
  passes, and so does a report with no findings at all.
  FAIL if the filename format is flagged at high or medium severity.
weight: 1
---

Does not report a format both ends reach through one shared module.
