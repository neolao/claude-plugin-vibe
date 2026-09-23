---
type: llm
focus: last_message
criteria: |
  `fetch_report` in fixtures/report_client.py caps attempts at
  `max_attempts`, passes `timeout=10` to `requests.get`, retries on any
  `requests.RequestException` (connection errors, timeouts, and non-2xx
  statuses via `raise_for_status`), sleeps with an exponential backoff
  between tries but not after the last one, and raises a final error naming
  both the url and the attempt count, chained `from` the last exception.

  PASS if no `high` or `medium` severity finding claims this call lacks a
  timeout, lacks a retry cap or backoff, lets network exceptions escape the
  retry loop, or loses the cause of the final failure.
  FAIL if it is flagged as a Timeout/limit or Lost context issue (or
  equivalent) at high or medium severity.
weight: 1
---

Does not flag the timed, capped, backed-off retry loop.
