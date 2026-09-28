---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Assertion precision` (or
  clearly equivalent category name, such as `Under-asserting`) finding on
  "charges full price under the threshold" in fixtures/test/cart.test.js,
  for asserting only `assert.ok(total)` (truthy) instead of the exact
  expected amount.
  FAIL if no finding flags the truthy-only `assert.ok(total)`.
weight: 1
---

Reports the truthy-only `assert.ok(total)` as an `Assertion precision`
finding.
