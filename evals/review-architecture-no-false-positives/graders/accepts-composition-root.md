---
type: llm
focus: last_message
criteria: |
  `fixtures/main.py` constructs `PostgresGateway` and injects it into
  `OrderService`, and `.vibe/modules/composition.md` declares it as the
  composition root. `core/order_service.py` builds nothing itself.

  PASS if no `high` or `medium` severity Wiring finding claims core
  instantiates its own adapters.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not call a declared composition root self-instantiation by core.
