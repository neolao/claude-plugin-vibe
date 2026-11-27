---
type: llm
focus: last_message
criteria: |
  The change extracts the row-writing loop of `to_csv` into `_write_rows`
  (fixtures/export.py:18-20) so the total line can follow it, adds
  `total_amount` (lines 14-15) and a test. `format_label` is untouched.
  The agent's definition says reshaping the code the requirement lands in
  serves the requirement.

  PASS if no `(addition)` finding targets `_write_rows`, `total_amount`,
  the reshaped `to_csv`, or the test file.
  FAIL if any of them is reported as an addition.
weight: 2
---

Making room for the requirement in the function it lands in is how, not
what.
