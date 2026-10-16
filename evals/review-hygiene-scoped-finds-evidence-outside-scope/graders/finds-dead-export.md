---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Dead code` (or clearly equivalent
  category name) finding on `export_invoices_xml` in
  fixtures/billing/export.py, a function nothing in the repository calls or
  imports (fixtures/cli/main.py imports only `export_invoices_csv`).
  FAIL if no finding flags `export_invoices_xml` as dead code.
weight: 1
---

Reports `export_invoices_xml` in fixtures/billing/export.py as a `Dead code`
finding. Neither export has a caller inside the scope: only a grep of the
whole repository separates the sibling the CLI imports from the one nothing
reaches.
