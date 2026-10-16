---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Coverage gap` (or clearly
  equivalent category name, such as `Missing negative cases`) finding on
  `invoiceTotal` in fixtures/src/billing/invoice.js, for its
  `throw new Error("empty invoice")` branch having no test in
  fixtures/tests/invoice.test.js.
  FAIL if no finding flags the untested empty-invoice branch, or if the
  finding claims the module has no tests at all (its tests exist in
  fixtures/tests/invoice.test.js; only this branch is uncovered).
weight: 1
---

Reports the one untested branch of the in-scope module after reading its
tests in fixtures/tests/, outside the path given — not the whole module as
untested.
