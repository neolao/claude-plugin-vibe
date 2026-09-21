---
type: llm
focus: last_message
criteria: |
  `OrderRepository` in fixtures/order_repository.py exposes `get`/`save`
  over domain `Order` objects — no rows, no query strings, no child
  entities.

  PASS if no `high` or `medium` severity Repository finding claims it leaks
  persistence details.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not call a collection-like repository of domain objects leaky.
