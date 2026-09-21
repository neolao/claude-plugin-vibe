---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Wiring` (or clearly equivalent
  category name) finding on `OrderService.__init__` in
  `fixtures/core/order_service.py`, for the core instantiating its own
  `PostgresGateway` adapter directly, with no composition root anywhere in
  the codebase wiring the dependency in instead.
  FAIL if no finding flags this self-instantiation.
weight: 1
---

Reports `OrderService.__init__`'s `PostgresGateway()` instantiation as a
Wiring finding.
