---
type: llm
focus: last_message
criteria: |
  fixtures/notifications/ has no `.vibe/modules/*.md` file.
  fixtures/core/order_service.py imports `notifications.templates`, and
  fixtures/notifications/smtp_notifier.py imports `core.ports`: a cycle
  between `core` and the unmapped zone, which no `Depends on` field
  declares.

  PASS if the reported findings include a `Circular dependency` (or
  clearly equivalent category name) finding naming the cycle between
  `core` and `notifications` — anchored on fixtures/core/order_service.py
  or on fixtures/notifications/smtp_notifier.py, naming either import as
  the edge that closes it.
  FAIL if no finding flags this cycle.
weight: 2
---

Reports a cycle closed through a zone the stale map has no module for.
