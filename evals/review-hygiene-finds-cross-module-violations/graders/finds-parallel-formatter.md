---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Duplication` (or clearly
  equivalent category name) finding that names both `format_amount` in
  fixtures/billing/money.py and `_money` in fixtures/billing/invoices.py as
  two implementations of the same cents-to-"EUR" amount formatting.
  FAIL if no finding names both functions as duplicated or parallel
  implementations.
weight: 1
---

Reports `format_amount` (money.py) and `_money` (invoices.py) as parallel
implementations of one concept, a `Duplication` finding.
