---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/src/billing/.
  fixtures/tests/rates.test.js tests fixtures/src/shipping/rates.js, a
  module outside the scope.

  PASS if no finding's FILE: line points to fixtures/tests/rates.test.js
  or to a file under fixtures/src/shipping/. A report with no findings at
  all passes.
  FAIL if any finding is anchored on rates.test.js (for example its
  `assert.ok(true)`) or on rates.js (for example its untested throw).
weight: 1
---

Leaves the tests of an out-of-scope module unreported, however poor they
are: the scope bounds what is reported.
