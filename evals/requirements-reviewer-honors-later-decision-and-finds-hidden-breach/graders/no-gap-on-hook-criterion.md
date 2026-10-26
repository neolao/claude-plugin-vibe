---
type: llm
focus: last_message
criteria: |
  Criterion 4 (the check runs after every stock movement) is met by
  `after_movement` in fixtures/hooks.py, which calls `warn_if_low`. The
  hook lives in another file than the warning logic.

  PASS if no finding reports criterion 4 as a gap, and no `(addition)`
  finding targets `hooks.py` or the test file.
  FAIL if either is reported.
weight: 1
---

A criterion met in another file than expected is met.
