---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Port ownership` (or clearly
  equivalent category name) finding on `OrderGatewayPort` in
  `fixtures/adapters/postgres_gateway.py`, for the port interface being
  defined on the adapter side instead of owned by `core`.
  FAIL if no finding flags `OrderGatewayPort`'s location as a
  port-ownership problem.
weight: 1
---

Reports `OrderGatewayPort` being defined inside the adapter module as a
Port ownership finding.
