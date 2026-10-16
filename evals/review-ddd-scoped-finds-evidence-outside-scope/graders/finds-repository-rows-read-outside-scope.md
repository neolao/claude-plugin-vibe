---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Repository` (or clearly
  equivalent category name) finding on `OrderRepository.find_unpaid` in
  fixtures/orders/order_repository.py for returning raw SQL rows
  (`fetchall()`) instead of `Order` objects like its sibling methods, whose
  ISSUE or SUGGESTION names the consumer reading those rows by column index
  in fixtures/dunning/reminders.py (`unpaid_order_notices`, `row[0]`,
  `row[1]`, `row[6]`).
  FAIL if no finding flags the raw rows, or if the finding never mentions
  fixtures/dunning/reminders.py or `unpaid_order_notices`.
weight: 1
---

Reports `find_unpaid` leaking raw rows as a Repository finding and names the
nightly job outside the scope that reads them by index: the cost of the leak
sits in the caller, which only an agent that greps the whole repository sees.
