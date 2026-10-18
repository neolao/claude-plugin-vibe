---
type: llm
focus: last_message
criteria: |
  Both bounds are included (`start <= date <= end`, line 5), rows outside
  are left out (the comprehension at line 11), and ISO strings compare
  correctly without a date library: every criterion and the constraint are
  met.

  PASS if no `(gap)` and no `(constraint)` finding is reported.
  FAIL if the agent reports a gap on inclusion of the bounds, on rows left
  out, or a constraint breach on date handling.
weight: 1
---

Met criteria are not gaps; string comparison of ISO dates is not a
date library.
