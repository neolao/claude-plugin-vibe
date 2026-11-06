---
type: llm
focus: last_message
criteria: |
  fixtures/services/order_service.py imports the concrete
  `OrderRepository` class from fixtures/repositories/order_repository.py
  and receives an instance by constructor from fixtures/main.py: the
  direction the map declares (services → repositories) and the layered
  convention the project follows. The driver (`psycopg2`) stays inside the
  repository.

  PASS if no `high` or `medium` severity Layer direction (or any other
  category) finding targets the `OrderRepository` import or the
  `repository: OrderRepository` constructor parameter of
  fixtures/services/order_service.py for depending on a concrete class.
  A report with no findings at all passes.
  FAIL if it is reported at high or medium severity.
weight: 1
---

Does not call a service importing its concrete repository class a bypassed
port or a wrong direction.
