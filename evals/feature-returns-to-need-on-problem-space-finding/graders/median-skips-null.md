---
type: llm
focus: { source: file, path: "src/stats.js" }
criteria: |
  `.vibe/decisions/001` says a statistics helper ignores `null` entries and
  computes on the remaining numbers; a list with no number left is the
  empty-list case.

  PASS if the new median function filters `null` (or `null`/`undefined`)
  out of the list before computing, computes the median on the remaining
  numbers, and throws the clear empty-list error only when no number is
  left.
  FAIL if a `null` entry makes the function throw, is treated as zero, or
  produces `NaN`.
weight: 3
---

The shipped code honours the project's recorded business rule, whichever
path of the loop got it there.
