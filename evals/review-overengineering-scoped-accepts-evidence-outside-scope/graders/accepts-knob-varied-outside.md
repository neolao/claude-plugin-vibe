---
type: llm
focus: last_message
criteria: |
  fixtures/src/notifications/service.py declares
  `NotificationService.__init__(self, channel, retry_count)`; its call
  sites, both outside the scope, pass `retry_count=3`
  (fixtures/src/billing/invoices.py) and `retry_count=1`
  (fixtures/src/billing/reminders.py).

  PASS if no `high` or `medium` severity `Unused configurability` (or
  clearly equivalent category name) finding targets `retry_count`. A
  `low` finding passes, and so does a report with no findings at all.
  FAIL if `retry_count` is reported as always receiving the same value at
  high or medium severity.
weight: 2
---

Does not call a parameter unused configurability when its call sites,
outside the scope, pass it different values.
