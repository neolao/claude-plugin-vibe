---
type: llm
focus: { source: file, path: "test/pricing.test.js" }
criteria: |
  PASS if a test now asserts the half-cent rounding case (an order or a
  rounding of 1.005 → 1.01, or an equivalent half-cent value), in a test
  that would have failed on the original helper.
  FAIL if no test covers it.
weight: 1
---

The reproducing test exists.
