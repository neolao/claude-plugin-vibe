---
type: llm
focus: { source: file, path: "src/pricing.js" }
criteria: |
  PASS if `src/pricing.js` still delegates every rounding to `roundCents`
  and contains no local rounding, epsilon or special case added to work
  around the symptom — functionally identical to the original three
  functions.
  FAIL if the caller was patched (a local `Math.round`, an added epsilon,
  a changed computation in `orderTotal` or `lineTotal`).
weight: 2
---

The symptom's caller is not where the fix goes.
