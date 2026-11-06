---
type: llm
focus: last_message
criteria: |
  fixtures/notifications/smtp_notifier.py has no `.vibe/modules/*.md`
  file. It imports `core.ports` only and is imported by fixtures/main.py,
  the declared composition root: the same inward direction the map
  declares for `adapters`. Nothing in `core/` imports it.

  PASS if no `high` or `medium` severity Module scope, Orphaned module,
  Circular dependency, Layer direction or Adapter purity finding targets
  fixtures/notifications/ for being absent from the map or undeclared in a
  `Depends on` field. A report with no findings at all passes.
  FAIL if the unmapped zone is reported at high or medium severity.
weight: 1
---

Does not report a zone the stale map has no module for when its imports
follow the declared direction.
