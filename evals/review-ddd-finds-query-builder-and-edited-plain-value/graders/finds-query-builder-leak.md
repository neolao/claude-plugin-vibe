---
type: llm
focus: last_message
criteria: |
  `OrderRepository.open_orders` in fixtures/orders/order_repository.py
  returns a SQLAlchemy `Query` over `OrderRecord` rows, and `overdue_report`
  in fixtures/reports/overdue.py keeps filtering and ordering it on
  `OrderRecord` columns before reading record fields, while `get` returns
  an `Order`.

  PASS if the reported findings include a `Repository` (or clearly
  equivalent category name) finding on `open_orders` or on
  `overdue_report` saying the query builder and/or the persistence records
  reach business code, with a suggestion along the lines of a finder that
  finishes the query and returns `Order`s (or a read-side query object).
  FAIL if no finding flags the query or the records handed out.
weight: 2
---

Reports the query builder handed to business code as a storage type leak.
