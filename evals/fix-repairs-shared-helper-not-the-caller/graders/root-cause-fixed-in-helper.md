---
type: llm
focus: { source: file, path: "src/money.js" }
criteria: |
  `roundCents(1.005)` returns 1 because `Math.round(100.49999…)` rounds
  down: the binary float of 1.005 × 100 is just under 100.5.

  PASS if `roundCents` in `src/money.js` was changed so that 1.005 rounds
  to 1.01 (an epsilon, `Number.EPSILON`, rounding on a string/exponent
  form, or an equivalent robust technique).
  FAIL if `src/money.js` is unchanged.
weight: 3
---

The fix lands in the shared helper, where the cause is.
