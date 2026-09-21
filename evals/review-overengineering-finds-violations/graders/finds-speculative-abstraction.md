---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Speculative abstraction` (or
  clearly equivalent category name) finding on the `NotificationChannel`
  abstract base class in fixtures/notification_system.py, for having exactly
  one implementation (`EmailChannel`) with nothing else in fixtures/
  registering a second channel into the extension point.
  FAIL if no finding flags `NotificationChannel` for this reason.
weight: 1
---

Reports `NotificationChannel` in fixtures/notification_system.py as a
`Speculative abstraction` finding.
