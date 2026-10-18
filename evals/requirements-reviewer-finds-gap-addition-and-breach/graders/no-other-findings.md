---
type: llm
focus: last_message
criteria: |
  Criteria 1 (CSV with date, amount, label) and 3 (file name
  `report-<YYYY-MM>.csv`) are met. The test file is an implementation detail
  that serves the request.

  PASS if no `(gap)` finding targets criterion 1 or 3, and no `(addition)`
  finding targets the test file, the header row, or the UTF-8 encoding.
  FAIL if any of those is reported.
weight: 1
---

Met criteria and supporting details are not findings.
