---
type: llm
focus: { source: file, path: "test/list-utils.test.js" }
criteria: |
  PASS if the test file now asserts that `max` of an all-negative list
  returns its largest element (e.g. `[-5, -2, -9]` → `-2`), in a test that
  would have failed on the original code.
  FAIL if no test covers an all-negative list.
weight: 1
---

The reproducing test exists in the project's test file.
