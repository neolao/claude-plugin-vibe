---
type: llm
focus: { source: file, path: "src/list-utils.js" }
criteria: |
  The bug: `max` starts from `let largest = 0`, so a list of negative
  numbers returns 0.

  PASS if `max` no longer seeds the result with 0 — it starts from the
  first element, from `-Infinity`, or an equivalent — so that
  `max([-5, -2, -9])` returns -2. An explicit empty-list error is fine.
  FAIL if the seed is still 0, or if the fix special-cases negative lists
  around an unchanged seed.
weight: 2
---

The root cause is fixed in the helper, not papered over.
