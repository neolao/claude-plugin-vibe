---
type: llm
focus: last_message
criteria: |
  fixtures/tests/test_rates.py is one of the two files in scope. Its only
  test calls `rate_for("EU")` and asserts `self.assertTrue(True)`: a
  `rate_for` returning any value, or the wrong one, passes it.

  PASS if a `Tautological` (or clearly equivalent category name, such as
  `Under-asserting` or `Assertion precision`) finding is anchored (its
  FILE: line) on fixtures/tests/test_rates.py and names the
  `assertTrue(True)` or the missing assertion on the returned rate.
  FAIL if no finding is anchored on fixtures/tests/test_rates.py, or if
  the report says that file is out of scope because the module it tests
  is.
weight: 2
---

A test file in scope is reviewed whatever it exercises: the module under
test being outside the path does not take the test out of scope.
