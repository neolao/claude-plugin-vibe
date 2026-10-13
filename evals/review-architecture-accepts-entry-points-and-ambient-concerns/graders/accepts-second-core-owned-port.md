---
type: llm
focus: last_message
criteria: |
  `NotifierPort` is defined in `core/ports.py` and implemented by `adapters/smtp_notifier.py`, whose `order_confirmed` returns nothing. `OrderService` receives both collaborators by injection and `main.py` builds them. `SmtpNotifier` names a technology in an adapter, and the port is named after the capability.

  PASS if no `high` or `medium` severity Port ownership, Leaky port, Adapter purity, or Wiring finding targets `NotifierPort`, `SmtpNotifier`, or `OrderService`'s construction.
  FAIL if it is reported at high or medium severity.
weight: 1
---

Does not invent a port, adapter, or wiring defect on a correct second adapter.
