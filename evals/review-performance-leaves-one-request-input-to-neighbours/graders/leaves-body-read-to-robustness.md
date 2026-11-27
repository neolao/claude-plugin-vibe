---
type: llm
focus: last_message
criteria: |
  `upload_trace` in fixtures/telemetry/app.py reads one request's body
  whole into `chunks` with no size cap before storing it. That is one
  request's input read whole into memory, which review-robustness owns as
  a missing limit; nothing it fills outlives the request.

  PASS if no `high` or `medium` severity finding of any category targets
  `upload_trace`, its `chunks` list or the body it reads. A `low` finding
  passes, a report with no findings at all passes, and so does a sentence
  outside any finding block saying the missing cap is review-robustness'
  (or review-web-security's).
  FAIL if `upload_trace`'s body read is reported as Unbounded (or any
  other category) at high or medium severity.
weight: 2
---

Leaves one request's input read whole to review-robustness.
