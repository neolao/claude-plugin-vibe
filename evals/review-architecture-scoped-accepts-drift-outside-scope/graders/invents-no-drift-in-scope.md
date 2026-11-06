---
type: llm
focus: last_message
criteria: |
  fixtures/core/order_service.py imports `core.discounts`, `core.ports`
  and `core.pricing` only; fixtures/core/pricing.py imports nothing. Both
  are listed in `.vibe/modules/core.md` and match its role; the ports are
  core-owned and injected by fixtures/main.py.

  PASS if no `high` or `medium` severity finding of any category targets
  fixtures/core/order_service.py or fixtures/core/pricing.py. A report
  with no findings at all passes.
  FAIL if either in-scope file is reported at high or medium severity.
weight: 1
---

Invents no drift in two in-scope files that match the map.
