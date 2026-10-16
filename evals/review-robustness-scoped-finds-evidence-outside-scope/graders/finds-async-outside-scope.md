---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Async` (or clearly equivalent
  category name) finding for `bus.publish(...)` being called without `await`
  in `hold_parcel` (fixtures/shipping/api.py). `publish` is an `async def`
  (fixtures/events/bus.py), so the call only creates a coroutine that never
  runs: the dashboards are never told the parcel is held, with no error
  raised.
  FAIL if no finding flags this unawaited call.
weight: 1
---

Reports the unawaited `bus.publish` in `hold_parcel`. api.py reads like a
plain function call; only events/bus.py, outside the scope, shows it is a
coroutine.
