---
type: llm
focus: last_message
criteria: |
  `OrderGatewayPort` is declared in `fixtures/core/ports.py` — inside the
  inner layer that depends on it, not on the adapter side.

  PASS if no `high` or `medium` severity Port ownership finding targets it.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not call a core-owned port misplaced.
