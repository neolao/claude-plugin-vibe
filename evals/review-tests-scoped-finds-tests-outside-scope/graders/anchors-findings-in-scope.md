---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/src/billing/. Its tests live
  in fixtures/tests/invoice.test.js; fixtures/tests/rates.test.js tests
  fixtures/src/shipping/rates.js, which is outside the scope.

  PASS if every finding's FILE: line points to fixtures/src/billing/ or to
  fixtures/tests/invoice.test.js.
  FAIL if any finding is anchored (its FILE: line) on
  fixtures/tests/rates.test.js or on a file under fixtures/src/shipping/
  — for example a finding on the `assert.ok(true)` in rates.test.js or on
  the untested throw in rates.js.
weight: 1
---

Reviews the tests of the in-scope code wherever they live, and nothing
else: a test that exercises only an out-of-scope module is not reported,
however poor it is.
