---
date: 2026-05-02
status: accepted
---
# The service follows ports & adapters (hexagonal architecture)
**Context:** Business rules and infrastructure were entangled, so pricing could
not be tested without a database and swapping the mail provider meant editing
domain code.
**Decision:** `core/` holds the domain and owns every port it needs, as an
interface defined inside `core/`. `adapters/` holds the driven adapters that
implement those ports. Dependencies point inward only, adapters never call each
other, and a composition root outside `core/` wires the concrete adapters in.
**Reason:** Keeps the domain testable in isolation and makes infrastructure
replaceable without touching business rules.
**Rejected alternatives:** A conventional layered service package — it leaves
the direction of dependencies implicit and drifts back within a release or two.
