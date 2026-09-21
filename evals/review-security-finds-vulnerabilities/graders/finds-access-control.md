---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Access control` (or clearly
  equivalent category name) finding on `export_all_invoices`, which takes a
  `requesting_user` argument, never uses it, and returns every customer's
  invoices to whoever calls it.
  FAIL if that missing authorization check is not flagged.
weight: 1
---

Reports the unchecked `requesting_user` in `export_all_invoices` as an Access
control finding.
