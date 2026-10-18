---
type: llm
focus: last_message
criteria: |
  Criterion 2 of the request ("Lines are sorted by date, oldest first") is
  not implemented: `to_csv` writes the rows in the order received, nothing
  sorts them.

  PASS if a `(gap)` finding quotes that criterion (or names criterion 2 /
  sorting by date) and says the export does not sort, with a fix.
  FAIL if no gap finding covers sorting.
weight: 2
---

The uncovered acceptance criterion is reported, citing the request.
