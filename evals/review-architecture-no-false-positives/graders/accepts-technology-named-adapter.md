---
type: llm
focus: last_message
criteria: |
  The port is `OrderGatewayPort`, named after its capability. The class
  named after its technology, `PostgresGateway`, is the adapter that
  implements it — an adapter is the one place a technology name belongs.

  PASS if no `high` or `medium` severity finding (Leaky port, Port
  ownership, or any other category) asks to rename `PostgresGateway` for
  carrying the technology in its name.
  FAIL if one does at high or medium severity.
weight: 1
---

Does not ask a Postgres adapter to drop "Postgres" from its name.
