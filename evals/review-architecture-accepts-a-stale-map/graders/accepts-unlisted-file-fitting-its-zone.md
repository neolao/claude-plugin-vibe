---
type: llm
focus: last_message
criteria: |
  fixtures/core/discounts.py is a pure function over a dict and two
  constants, imported by fixtures/core/order_service.py. It fits the role
  `.vibe/modules/core.md` declares ("pure business/domain logic ... no I/O,
  no framework, database, or mail imports") but that module's `Files:` list
  does not mention it: the map predates the file.

  PASS if no `high` or `medium` severity Module scope (or any other
  category) finding targets fixtures/core/discounts.py or the `core` module
  for a file the map does not list. A report with no findings at all
  passes.
  FAIL if the unlisted file is reported at high or medium severity.
weight: 2
---

Does not report a file the stale map omits when its purpose fits the zone's
role.
