---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Shotgun surgery` (or clearly
  equivalent category name) finding on the currency code "EUR" hardcoded in
  fixtures/orders/pricing.py (`total_label`) that names at least one of its
  other copies outside the scope: fixtures/invoicing/render.py or
  fixtures/notifications/email.py.
  FAIL if no finding flags the "EUR" literal as a concept duplicated across
  files, or if the finding names no file outside fixtures/orders/.
weight: 1
---

Reports the "EUR" literal in fixtures/orders/pricing.py as Shotgun surgery
and names a copy in fixtures/invoicing/ or fixtures/notifications/. Inside
the scope the literal appears once: the repetition is only visible to an
agent that greps the whole repository.
