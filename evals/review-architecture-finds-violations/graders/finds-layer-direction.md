---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Layer direction` (or clearly
  equivalent category name) finding on `fixtures/core/order_service.py`,
  for the domain/core module importing `psycopg2` (a concrete database
  driver) and executing SQL directly instead of going through a port.
  FAIL if no finding flags this driver import from core.
weight: 1
---

Reports core's direct `psycopg2` import/usage as a Layer direction finding.
