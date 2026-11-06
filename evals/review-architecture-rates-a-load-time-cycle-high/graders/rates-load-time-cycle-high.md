---
type: llm
focus: last_message
criteria: |
  fixtures/core/order_service.py imports `PostgresGateway` from
  `adapters.postgres_gateway` at module level, before `OrderRecord` is
  defined; fixtures/adapters/postgres_gateway.py imports `OrderRecord`
  from `core.order_service` at module level. fixtures/main.py imports
  `core.order_service` first: Python loads `adapters.postgres_gateway`
  while `core.order_service` is still partially initialized, and the
  `from core.order_service import OrderRecord` line raises `ImportError`
  — nothing in the application can be imported.

  PASS if the reported findings include a `Circular dependency` (or
  clearly equivalent category name) finding on this core/adapters cycle
  whose SEVERITY is `high`, and whose ISSUE says the cycle fails at import
  or load time (or words to that effect: raises, cannot be imported,
  partially initialized).
  FAIL if the cycle is not reported, or is reported at medium or low
  severity, or at high severity without naming the load-time failure.
weight: 2
---

Rates a cycle that breaks at load `high`: the structure fails at run time,
not only on principle.
