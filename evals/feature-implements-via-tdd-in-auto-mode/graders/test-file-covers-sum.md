---
type: llm
focus: { source: file, path: "test/stats.test.js" }
criteria: |
  PASS if the test file now contains tests for the new sum function: at
  least one nominal sum, and one asserting that non-numeric input raises
  (e.g. `assert.throws` with a message pattern).
  FAIL if the test file is unchanged or covers only the nominal case.
weight: 1
---

The implementer wrote the tests in the project's test file, nominal and
error path included.
