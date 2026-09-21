---
type: llm
focus: last_message
criteria: |
  The fixtures implement a small hexagonal-style app that already follows
  every rule the checklist tests, in ways that could superficially look
  like violations: `core/ports.py` defines `OrderGatewayPort` inside
  `core/`, owned by the inner layer (not the adapter side);
  `core/order_service.py` takes its gateway through constructor injection
  with no `psycopg2` import and no raw SQL (matches
  `.vibe/modules/core.md`'s declared role, honors decision 002, and is the
  only place `calculate_total` is used — no responsibility spread);
  `adapters/postgres_gateway.py` implements that port, imports `psycopg2`
  and a DB DSN constant (expected — adapters are allowed to know the
  driver), calls no other adapter, and its `save` returns `None` rather
  than a raw row (not a leaky port); `adapters/config.py` is only imported
  from one place but that one place is real, current usage (not an
  orphaned module); `main.py` is a genuine composition root that
  constructs the concrete adapter and injects it into `OrderService` (not
  "core instantiating its own adapters"); there is no cycle between `core`
  and `adapters` (only `adapters` imports from `core`, matching the module
  map's declared dependency direction).

  PASS if the response reports no `high` or `medium` severity architecture
  finding on this code — either no findings at all, or only `low` severity
  style notes unrelated to these already-correct patterns.
  FAIL if it flags `OrderGatewayPort`'s location as a port-ownership
  problem, `postgres_gateway.py`'s driver usage as a layer-direction or
  adapter-purity violation, `PostgresGateway.save`'s return value as a
  leaky port, `adapters/config.py` as orphaned, `main.py`'s composition
  root as core instantiating adapters, or invents a circular dependency,
  module scope drift, responsibility spread, or decision violation
  anywhere in this code.
weight: 2
---

Does not invent architecture findings on a codebase that already follows
ports-and-adapters correctly.
