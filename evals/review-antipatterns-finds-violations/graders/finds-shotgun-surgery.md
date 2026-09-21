---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Shotgun surgery` (or clearly
  equivalent category name) finding naming the currency code ("USD") as a
  literal duplicated across fixtures/date_utils.py, fixtures/pricing_rules.py,
  and fixtures/order_workflow.py — one conceptual change (changing the
  currency) would require touching all of them.
  FAIL if no finding names this concept duplicated across the files.
weight: 1
---

Names the "USD" literal duplicated across multiple files as a Shotgun
surgery finding.
