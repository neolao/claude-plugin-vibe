---
type: regex
target:
  source: file
  path: test/pricing.test.js
pattern: "1\\.005[\\s\\S]{0,200}?1\\.01"
weight: 1
---

The reproducing test exists: the test file asserts that the reported price,
1.005, comes out as 1.01. The original helper returns 1 for it, so such an
assertion fails before the fix. A regex, not an `llm` grader: asked whether
the test "would have failed on the original helper", the judge reasoned about
float rounding and split its votes on a correct test.
