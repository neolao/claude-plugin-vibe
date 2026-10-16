---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/src/billing/. Its tests live
  outside that path, in fixtures/tests/invoice.test.js: `invoiceTotal` has
  a literal-expected sum test and an `assert.throws` on the empty-invoice
  branch; `billingAddress` has an awaited address test and an
  `assert.rejects` on the unknown-customer branch. Every branch of the
  module is covered.

  PASS if no `high` or `medium` severity Coverage gap, Missing negative
  cases or Under-asserting finding claims that `invoiceTotal` or
  `billingAddress` is untested or that one of their error branches lacks a
  test, and the report never says the module or the scope has no tests. A
  report with no findings at all passes.
  FAIL if either function, or one of its branches, is reported as untested
  at high or medium severity, or if the report says no tests were found
  for the scope.
weight: 2
---

Does not call a module untested because its tests sit outside the path
under review.
