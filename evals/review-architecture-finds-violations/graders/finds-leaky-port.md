---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Leaky port` (or clearly
  equivalent category name) finding on `PostgresGateway.save` in
  `fixtures/adapters/postgres_gateway.py`, for returning a raw database
  cursor/row instead of a domain type.
  FAIL if no finding flags this technology type leaking through the port.
weight: 1
---

Reports `PostgresGateway.save` returning a raw DB row/cursor as a Leaky
port finding.
