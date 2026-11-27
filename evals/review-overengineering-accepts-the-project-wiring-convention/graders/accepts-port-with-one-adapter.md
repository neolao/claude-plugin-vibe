---
type: llm
focus: last_message
criteria: |
  fixtures/CLAUDE.md declares ports & adapters; the tree carries
  src/core/ports/ and src/adapters/. `OrderRepository` in
  fixtures/src/core/ports/order_repository.py is implemented by one
  adapter, `PostgresOrderRepository` in
  fixtures/src/adapters/postgres/order_repository.py, and used by
  `PlaceOrder` in the core.

  PASS if no `high` or `medium` severity `Speculative abstraction` (or
  clearly equivalent category name) finding targets `OrderRepository`
  for having a single implementation. A `low` finding passes, and so
  does a report with no findings at all.
  FAIL if `OrderRepository` is reported as a one-implementation
  interface or base class at high or medium severity.
weight: 2
---

Does not call a port with its single adapter speculative in a project
that explicitly follows ports & adapters: one adapter per port is that
architecture's designed shape.
