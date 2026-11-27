---
type: llm
focus: last_message
criteria: |
  `fanout` in fixtures/app.py refuses more than `MAX_CONTACTS` contacts
  and submits each to `notifier`, a `ThreadPoolExecutor` of four workers
  created once at import: no request starts a thread of its own.

  PASS if no `high` or `medium` severity `DoS` (or clearly equivalent
  category name) finding targets `fanout`, `notifier` or `notify`. A
  `low` finding passes, and so does a report with no findings at all.
  FAIL if the fan-out is reported as unbounded concurrency at high or
  medium severity.
weight: 2
---

Does not call a bounded pool fed a capped list a DoS.
