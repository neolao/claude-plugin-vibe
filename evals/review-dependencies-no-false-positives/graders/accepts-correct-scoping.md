---
type: llm
focus: last_message
criteria: |
  The four declared packages are all used where they are declared:
  `express`, `lodash` and `date-fns` are production dependencies required by
  fixtures/src/index.js; `jest` is a devDependency and is the test runner for
  fixtures/test/index.test.js — Jest provides `test` and `expect` as
  globals, so that file has no `require("jest")`, and runtime code never
  uses jest.

  PASS if no `high` or `medium` severity Unused or Misplaced finding targets
  `express`, `lodash`, `date-fns` or `jest`. A report with no findings at
  all passes.
  FAIL if any is flagged at high or medium severity.
weight: 1
---

Does not call correctly scoped, actually-imported dependencies unused or misplaced.
