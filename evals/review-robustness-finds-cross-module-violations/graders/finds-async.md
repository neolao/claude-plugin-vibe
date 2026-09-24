---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Async` (or clearly equivalent
  category name) finding for `audit.record(...)` being called without
  `await` in `adjust_stock` (fixtures/inventory/api.py). `record` is an
  `async def` (fixtures/inventory/audit.py), so the call only creates a
  coroutine that never runs: the audit line for a manual stock change is
  never written, with no error raised.
  FAIL if no finding flags this unawaited call.
weight: 1
---

Reports the unawaited `audit.record` in `adjust_stock`. api.py reads like a
plain function call; only audit.py shows it is a coroutine.
