---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Dead code` (or clearly equivalent
  category name) finding on `export_orders_xml` in
  fixtures/billing/export.py, for a function no module in fixtures/ calls or
  imports (cli.py imports only `export_orders_csv`).
  FAIL if no finding flags `export_orders_xml` as dead code.
weight: 1
---

Reports `export_orders_xml` in fixtures/billing/export.py as a `Dead code`
finding. Seeing it takes a cross-file check: the function is defined and
looks used-shaped, only cli.py's imports show nothing reaches it.
