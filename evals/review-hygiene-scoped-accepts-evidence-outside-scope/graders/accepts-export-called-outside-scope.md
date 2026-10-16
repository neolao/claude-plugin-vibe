---
type: llm
focus: last_message
criteria: |
  `export_invoices_csv` in fixtures/billing/export.py has no caller inside
  the scope (fixtures/billing/), but fixtures/cli/main.py imports it (via
  the `billing` package) and calls it for the `export` command.

  PASS if no `high` or `medium` severity finding calls `export_invoices_csv`
  dead or unused code. A report with no findings at all passes.
  FAIL if it is flagged as Dead code (or equivalent) at high or medium
  severity.
weight: 1
---

Does not call a function dead when its only caller sits outside the path
under review.
