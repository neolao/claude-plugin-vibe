---
type: llm
focus: last_message
criteria: |
  `Clock` in fixtures/clock.py has one production implementation, but
  `FrozenClock` and `test_frozen_clock_returns_fixed_time` in the same file
  exercise the seam.

  PASS if no `high` or `medium` severity Speculative abstraction finding
  targets it.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not call a test seam that tests actually use speculative.
