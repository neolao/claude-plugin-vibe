---
type: llm
focus: last_message
criteria: |
  PASS if the reply requires row-level errors to say what's wrong (bad email,
  duplicate username, missing field) and how to fix it, next to the failing
  row, rather than a single aggregate error message — e.g. "each rejected row
  shows its own reason and the row number" or a test scenario checking a
  specific row's error is shown next to that row.
  FAIL if the reply only mentions errors generically ("show validation
  errors") without tying the requirement to per-row, actionable, in-place
  messaging for this CSV import.
weight: 2
---

Requires per-row, actionable, in-place error messages for the failed CSV
rows, not a generic "show errors" statement.
