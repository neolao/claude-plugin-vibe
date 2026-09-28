---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Coverage gap` (or clearly
  equivalent category name, such as `Missing negative cases`) finding on
  `cartTotal` in fixtures/src/cart.js, for its `throw new Error("empty
  cart")` branch having no test in either fixtures/test/ or fixtures/e2e/.
  FAIL if no finding flags the untested empty-cart branch.
weight: 1
---

Reports `cartTotal`'s untested empty-cart branch as a `Coverage gap`
finding.
