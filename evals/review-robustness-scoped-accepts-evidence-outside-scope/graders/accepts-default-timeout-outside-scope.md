---
type: llm
focus: last_message
criteria: |
  `dispatch_parcel` in fixtures/shipping/dispatch.py calls `get_json`
  without passing a `timeout`, but `get_json` (fixtures/carriers/http.py)
  defaults `timeout` to `DEFAULT_TIMEOUT = 10` seconds, so the carrier call
  is bounded.

  PASS if no `high` or `medium` severity finding claims this call has no
  timeout, waits forever, or hangs the scanner thread. A report with no
  findings at all passes.
  FAIL if it is flagged as a Timeout/limit issue (or equivalent) at high or
  medium severity.
weight: 1
---

Does not call a call unbounded when the helper outside the path under review
supplies the timeout.
