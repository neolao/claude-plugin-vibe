---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Repository` (or clearly
  equivalent category name) finding on `OrderRepository` in
  fixtures/order_repository.py, for `find_by_id` returning a raw `dict` (the
  SQL row) instead of a domain `Order` object, leaking persistence/query
  details to callers instead of exposing a collection-like abstraction over
  domain objects.
  FAIL if no finding flags this raw-row leakage.
weight: 1
---

Reports `OrderRepository.find_by_id` returning a raw row instead of a domain
object as a Repository finding.
