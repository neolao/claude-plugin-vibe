---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Primitive obsession` (or clearly
  equivalent category name) finding on `InvoiceFormatter.format` /
  `customer.balance_cents` in fixtures/pricing_rules.py, for representing
  money as a bare integer of cents instead of a dedicated Money type.
  FAIL if no finding flags this bare-integer money representation.
weight: 1
---

Reports the bare-integer `balance_cents` money representation as a
Primitive obsession finding.
