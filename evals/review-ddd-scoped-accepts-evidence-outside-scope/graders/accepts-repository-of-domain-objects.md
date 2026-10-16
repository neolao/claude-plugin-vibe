---
type: llm
focus: last_message
criteria: |
  `OrderRepository` in fixtures/orders/order_repository.py returns `Order`
  objects from `get`, `find_for_customer` and `find_unpaid`, keeps its SQL
  and `sqlite3` connection to itself, and is called from outside the scope
  by use cases (`PlaceOrder`, `CustomerOrders` in fixtures/checkout/) and the
  nightly job in fixtures/dunning/reminders.py, which all handle `Order`s,
  never rows.

  PASS if no `high` or `medium` severity Repository finding claims it leaks
  rows, query strings or storage types to its callers, that it returns raw
  data instead of domain objects, or that the domain calls it directly
  instead of through a use case. A report with no findings at all passes.
  FAIL if it is flagged for one of those reasons at high or medium severity.
weight: 1
---

Does not call a collection-like repository leaky when its callers outside the
path under review receive domain objects.
