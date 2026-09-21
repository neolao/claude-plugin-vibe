---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Leftover` (or clearly equivalent
  category name) finding on fixtures/notifications.py's `send_notification`,
  for either the `print(f"DEBUG: ...")` debug artifact or the commented-out
  `old_client = LegacyMailer()` block (or both) left in the function.
  FAIL if neither the debug print nor the commented-out block is flagged as a
  Leftover finding.
weight: 1
---

Reports the debug `print` and/or the commented-out block in
fixtures/notifications.py's `send_notification` as a `Leftover` finding.
