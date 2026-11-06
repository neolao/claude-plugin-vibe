---
type: llm
focus: last_message
criteria: |
  `OrderRepository.find_overdue` in fixtures/orders/order_repository.py
  finishes its SQLAlchemy query inside the repository and returns `Order`s;
  `OverdueReportQuery` in fixtures/reports/overdue.py is a read-side query
  that computes the finance report in SQL and returns `OverdueRow`
  projections, never an `Order` and never a live query.

  PASS if no `high` or `medium` severity Repository (or Domain isolation)
  finding claims `find_overdue` leaks a query or rows, that
  `OverdueReportQuery` is a repository that should return domain objects,
  or that its `OverdueRow` projection is a leak. A report with no findings
  at all passes.
  FAIL if either is flagged for one of those reasons at high or medium
  severity.
weight: 1
---

Leaves alone a repository method that finishes its query and a read-side
query object returning projections.
