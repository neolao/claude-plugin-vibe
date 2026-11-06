---
type: llm
focus: last_message
criteria: |
  The scope is fixtures/promotions/. The shop holds other defects whose
  every file is outside it: fixtures/dunning/reminders.py reads raw rows
  from `find_unpaid` of fixtures/orders/order_repository.py; `reroute` in
  fixtures/orders/order.py edits the `Address` of
  fixtures/customers/address.py in place; fixtures/orders/ calls the
  customer a buyer while fixtures/customers/, fixtures/checkout/ and
  fixtures/api/ call it a customer.

  PASS if every finding's FILE: line points to a file under
  fixtures/promotions/, and no finding (whatever its FILE: line) reports
  the dunning rows, the address edited in place, or the buyer / customer
  split as its own defect. Naming fixtures/orders/order.py as the aggregate
  that bundles.py writes is fine.
  FAIL if any finding is anchored outside fixtures/promotions/, or if one
  of those three defects is reported.
weight: 1
---

Leaves a defect with both ends outside the scope to the full review.
