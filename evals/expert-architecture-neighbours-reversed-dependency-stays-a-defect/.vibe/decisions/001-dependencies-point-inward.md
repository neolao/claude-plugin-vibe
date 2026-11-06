---
date: 2026-02-09
status: accepted
---
# Dependencies point inward: core owns its ports, adapters implement them
**Context:** The first invoice feature was tested against a real S3 bucket because the service called the storage client directly; a bucket outage failed the unit tests.
**Decision:** `core/` imports nothing from `adapters/` or `app.py`. When a core service needs infrastructure, it declares the need as a port it owns (a protocol or a callable it receives), `adapters/` implements it, and `app.py` wires the implementation in.
**Reason:** Core stays testable with fakes, and infrastructure is replaceable without touching business rules.
**Rejected alternatives:** Mocking the storage client inside core tests — keeps the client's types in business code.
