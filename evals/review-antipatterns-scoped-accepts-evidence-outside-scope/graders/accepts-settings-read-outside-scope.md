---
type: llm
focus: last_message
criteria: |
  `SMTP_HOST`, `SMTP_PORT` and `SMTP_TIMEOUT_SECONDS` in
  fixtures/orders/settings.py have no reader inside the scope
  (fixtures/orders/), but fixtures/notifications/mailer.py imports and uses
  all three.

  PASS if no `high` or `medium` severity Cargo cult (or dead-configuration)
  finding targets these constants. A report with no findings at all passes.
  FAIL if they are flagged at high or medium severity as unread or leftover
  configuration.
weight: 1
---

Does not call settings cargo cult when their reader sits outside the path
under review.
