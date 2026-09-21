---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Layer direction` (or clearly
  equivalent category name) finding on `fixtures/core/order_service.py`,
  for the domain/core module importing `psycopg2` (a concrete database
  driver) and calling it in `ping_storage` instead of going through a port
  owned by core.
  FAIL if no finding flags this driver import from core.
weight: 1
---

Reports `core/order_service.py` importing and calling a concrete database
driver as a `Layer direction` finding.
