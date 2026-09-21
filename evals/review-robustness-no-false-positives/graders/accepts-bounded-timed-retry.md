---
type: llm
focus: last_message
criteria: |
  `fetch_report` in fixtures/report_client.py caps attempts at
  `max_attempts`, sleeps with an exponential backoff between tries, passes
  `timeout=10` to `requests.get`, and raises a final error naming both the
  url and the attempt count.

  PASS if no `high` or `medium` severity finding claims this call lacks a
  timeout, lacks a retry cap, or lacks backoff.
  FAIL if it is flagged as a Timeout/limit issue (or equivalent) at high or
  medium severity.
weight: 1
---

Does not flag the timed, capped, backed-off retry loop.
