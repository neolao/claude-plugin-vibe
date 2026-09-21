---
date: 2026-06-10
status: accepted
---
# Core never talks to the database directly
**Context:** Reporting and order placement used to open their own DB
connections, tying business rules to a specific driver and making them
impossible to unit test without a real Postgres instance.
**Decision:** All SQL and driver calls live in `adapters/`. `core/` may only
call the `OrderGatewayPort` interface it owns; it must never import a database
driver or execute a query directly.
**Reason:** Keeps pricing rules testable in isolation and lets the storage
engine change without touching business logic.
**Rejected alternatives:** An ORM imported directly into `core/` — still couples
business logic to a specific persistence technology.
