---
type: llm
focus: last_message
criteria: |
  fixtures/src/orders/repository.py declares the abstract base class
  `OrderRepository`; `SqlOrderRepository` in
  fixtures/src/orders/sql_repository.py is its only implementation, and
  run_billing.py builds `SqlOrderRepository(db)` directly. Nothing in
  fixtures/ declares ports & adapters: no CLAUDE.md, no ADR, no `ports/`
  or `adapters/` directory.

  PASS if the reported findings include a `Speculative abstraction` (or
  clearly equivalent category name) finding whose FILE: line points to
  fixtures/src/orders/repository.py and that names `OrderRepository` as
  a base class or interface with a single implementation.
  FAIL if no finding reports `OrderRepository` for this reason. A
  separate finding on `SqlOrderRepository` itself as a pattern without
  need is neither required nor counted here.
weight: 2
---

Reports a one-implementation interface in a layered project: without a
declared hexagon, the port exemption does not apply.
