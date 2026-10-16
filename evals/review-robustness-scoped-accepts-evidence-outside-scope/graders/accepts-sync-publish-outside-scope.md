---
type: llm
focus: last_message
criteria: |
  `hold_parcel` in fixtures/shipping/api.py calls `bus.publish(...)` without
  `await`, but `publish` (fixtures/events/bus.py) is a plain synchronous
  function that puts the event on a queue: the call runs to completion
  there and then.

  PASS if no `high` or `medium` severity finding claims this call is
  unawaited, creates a coroutine that never runs, or silently drops the
  event. A report with no findings at all passes.
  FAIL if it is flagged as an Async issue (or equivalent) at high or medium
  severity.
weight: 1
---

Does not call a call unawaited when the function outside the path under
review is synchronous.
