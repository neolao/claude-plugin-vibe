---
type: llm
focus: last_message
criteria: |
  Criterion 1 (the CSV ends with `total,<sum>`) is met by the
  `writer.writerow(["total", total_amount(rows)])` line of `to_csv`, and
  criterion 2 (rounded to two decimals) by `round(..., 2)` in
  `total_amount`. The signature of `export_report(rows, month)` is
  unchanged. `total_amount` and the new test serve the request.

  PASS if no `(gap)` finding targets criterion 1 or 2, no `(constraint)`
  finding targets the signature, and no `(addition)` finding targets
  `total_amount`, the total line, or the test file.
  FAIL if any of those is reported.
weight: 1
---

A helper and a test that serve a requirement are how, not what.
