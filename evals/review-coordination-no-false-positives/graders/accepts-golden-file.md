---
type: llm
focus: last_message
criteria: |
  fixtures/tests/golden/export_sample.csv carries the header
  `reference,status,priority` that `COLUMNS` in fixtures/reports/export.py
  writes; fixtures/tests/test_export.py compares a real export with that
  file.

  PASS if no `high` or `medium` severity finding names the golden CSV,
  fixtures/tests/golden/export_sample.csv or `COLUMNS` as a copied
  constant, a producer/reader format or any coordination to maintain. A
  `low` finding passes, and so does a report with no findings at all.
  FAIL if the golden file or the CSV header is flagged at high or medium
  severity.
weight: 1
---

Does not report a snapshot file a test compares the output with: it is
the guard, not a copy to maintain.
