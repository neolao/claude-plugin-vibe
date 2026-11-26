---
type: regex
target:
  source: file
  path: test/list-utils.test.js
pattern: "max\\(\\s*\\[\\s*-\\d+(?:\\.\\d+)?(?:\\s*,\\s*-\\d+(?:\\.\\d+)?)+\\s*\\]\\s*\\)"
weight: 1
---

The reproducing test exists: the test file calls `max` on a list made only of
negative numbers (such as the reported `[-5, -2, -9]`). The original fixture
has no such call, and the original code returns 0 for it. A regex, not an
`llm` grader: asked whether the test "would have failed on the original
code", the judge split its votes on a test asserting `max([-5, -2, -9])` is
-2 verbatim.
