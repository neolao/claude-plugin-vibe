---
type: llm
focus: last_message
criteria: |
  Two rows in the table record a deliberate user choice, not a project fact:
  `review-tests` ("no test suite, by deliberate choice") and
  `review-security` ("covered by the platform team's own scanner, explicit
  opt-out"). Step 1 is explicit that a deliberate user choice is never
  overridden — even though `test_app.py` exists in the codebase, which would
  otherwise contradict the `review-tests` reason.

  PASS if neither `review-tests` nor `review-security` was activated, and the
  report does not claim to have flipped either row.
  FAIL if either agent was run or reported as flipped to active.
weight: 2
---

Leaves the two rows recording a deliberate user choice alone, including the
one a project fact would otherwise contradict.
