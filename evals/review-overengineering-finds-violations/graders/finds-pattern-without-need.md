---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Pattern without need` (or clearly
  equivalent category name) finding on `NotificationChannelFactory` in
  fixtures/notification_system.py, for a factory whose `create` method always
  builds the same `EmailChannel` — a direct instantiation would do the same
  job without the indirection.
  FAIL if no finding flags `NotificationChannelFactory` for this reason.
weight: 1
---

Reports `NotificationChannelFactory` in fixtures/notification_system.py as a
`Pattern without need` finding.
