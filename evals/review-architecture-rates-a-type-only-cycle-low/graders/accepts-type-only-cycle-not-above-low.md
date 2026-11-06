---
type: llm
focus: last_message
criteria: |
  fixtures/billing/invoice.py imports `shipping.schedule` at module level,
  the direction `.vibe/modules/billing.md` declares.
  fixtures/shipping/schedule.py names `billing.invoice.Invoice` only under
  `if TYPE_CHECKING:`, with `from __future__ import annotations`, for the
  annotation of `eta_for`: at run time no import of `billing` happens,
  nothing loads and nothing fails. The cycle exists for a type checker
  only.

  PASS if no `high` or `medium` severity Circular dependency (or Layer
  direction, or any other category) finding targets the billing/shipping
  cycle or the `TYPE_CHECKING` import of fixtures/shipping/schedule.py. A
  `low` finding on it passes, as does a report with no findings at all.
  FAIL if the type-only cycle is reported at high or medium severity.
weight: 2
---

Does not rate a cycle only a type-only import closes above `low`.
