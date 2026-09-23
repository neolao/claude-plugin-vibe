---
type: llm
focus: last_message
criteria: |
  `Clock` in fixtures/clock.py has one production implementation
  (`SystemClock`), but `SessionExpiry` takes any `Clock`, and
  `test_session_expires_after_ttl` injects `FrozenClock` into it to exercise
  the seam.

  PASS if no `high` or `medium` severity Speculative abstraction finding
  targets it.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not call a test seam that tests actually use speculative.
