---
type: llm
focus: last_message
criteria: |
  fixtures/src/notifications/channel.py declares the abstract base class
  `NotificationChannel` with `EmailChannel` in the same file; a second
  implementation, `SmsChannel`, lives in fixtures/src/sms/sms_channel.py,
  outside the scope, and fixtures/src/billing/reminders.py builds it.

  PASS if no `high` or `medium` severity `Speculative abstraction` (or
  clearly equivalent category name) finding targets `NotificationChannel`
  or `EmailChannel`. A `low` finding passes, and so does a report with
  no findings at all.
  FAIL if `NotificationChannel` is reported as a base class or interface
  with a single implementation at high or medium severity.
weight: 2
---

Does not call a base class speculative when its second implementation
sits outside the scope: the scope bounds what is reported, not what is
read.
