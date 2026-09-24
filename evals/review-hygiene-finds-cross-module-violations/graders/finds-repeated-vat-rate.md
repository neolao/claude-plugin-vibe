---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Duplication` (or clearly
  equivalent category name) finding on the `0.2` VAT rate (or the
  "add 20% VAT" computation built on it) repeated across
  fixtures/billing/checkout.py, fixtures/billing/invoices.py and
  fixtures/billing/refunds.py, naming at least two of those three files and
  suggesting one named constant or one shared helper.
  FAIL if no finding flags the repeated `0.2` rate or VAT computation across
  files.
weight: 1
---

Reports the `0.2` VAT rate repeated in checkout.py, invoices.py and
refunds.py as a `Duplication` finding (a magic value deserving one named
constant).
