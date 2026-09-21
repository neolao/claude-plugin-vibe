---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Feature envy` (or clearly
  equivalent category name) finding on `InvoiceFormatter.format` in
  fixtures/pricing_rules.py, for a method that mostly reads and combines
  another object's (`Customer`'s) fields instead of doing its own work.
  FAIL if no finding flags `InvoiceFormatter.format` for this reason.
weight: 1
---

Reports `InvoiceFormatter.format` reaching into `Customer`'s data as a
Feature envy finding.
