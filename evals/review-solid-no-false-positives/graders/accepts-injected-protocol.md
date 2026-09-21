---
type: llm
focus: last_message
criteria: |
  `OrderProcessor` receives its `PaymentGateway` as a constructor-injected
  `Protocol`; it never constructs a concrete client.

  PASS if no `high` or `medium` severity `D` finding claims a dependency on
  a concretion here.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not call a constructor-injected Protocol a DIP violation.
