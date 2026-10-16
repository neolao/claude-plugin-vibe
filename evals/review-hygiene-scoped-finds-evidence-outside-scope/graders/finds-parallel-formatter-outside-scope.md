---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Duplication` (or clearly
  equivalent category name) finding on `_amount` in
  fixtures/billing/invoices.py that names `format_amount` in
  fixtures/reports/money.py as the other implementation of the same
  cents-to-"EUR" amount formatting.
  FAIL if no finding flags `_amount` as a parallel implementation, or if the
  finding never names fixtures/reports/money.py (or `format_amount`).
weight: 1
---

Reports `_amount` (fixtures/billing/invoices.py) and `format_amount`
(fixtures/reports/money.py) as parallel implementations of one concept, a
`Duplication` finding anchored in scope. Inside fixtures/billing/ the
formatter exists once: its twin is only visible to an agent that greps the
whole repository.
