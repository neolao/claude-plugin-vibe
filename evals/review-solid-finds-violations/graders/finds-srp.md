---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `S` (or clearly equivalent SRP)
  finding on `NotificationSender.send` in fixtures/app.py, for mixing message
  normalization, channel selection, and direct I/O (SMTP, HTTP) in one method.
  FAIL if no finding points at this method for mixing those concerns.
weight: 1
---

Reports `NotificationSender.send` mixing parsing/normalization, dispatch
decision, and I/O as an `S` finding.
