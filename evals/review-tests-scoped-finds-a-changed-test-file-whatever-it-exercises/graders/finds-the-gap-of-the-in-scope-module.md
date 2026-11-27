---
type: llm
focus: last_message
criteria: |
  fixtures/billing/invoice.py is in scope; its tests live in
  fixtures/tests/test_invoice.py, outside the scope, which covers the sum
  and not the `raise ValueError("empty invoice")` branch.

  PASS if a `Coverage gap` (or clearly equivalent category name, such as
  `Missing negative cases`) finding is anchored (its FILE: line) on
  fixtures/billing/invoice.py for the untested empty-invoice branch, and
  no finding claims `invoice_total` has no tests at all.
  FAIL if no finding reports the untested empty-invoice branch, or if a
  finding says the module is untested.
weight: 1
---

Reads the tests of the in-scope module where they live and reports its
one uncovered branch, not the whole module as untested.
