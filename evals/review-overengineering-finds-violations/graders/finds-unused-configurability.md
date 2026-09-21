---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Unused configurability` (or
  clearly equivalent category name) finding on `NotificationService`'s
  `retry_count` parameter in fixtures/notification_system.py, for being
  passed as the literal `3` at both call sites (`send_welcome_email` and
  `send_password_reset_email`) — a configuration option that never actually
  varies.
  FAIL if no finding flags `retry_count` for always holding the same value.
weight: 1
---

Reports `retry_count` in fixtures/notification_system.py always being `3` as
an `Unused configurability` finding.
