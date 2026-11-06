---
type: llm
focus: last_message
criteria: |
  The tracking page will show the estimate when it is there; during the
  rollout three pods still publish messages without the field, the bus
  keeps seven days of messages published before the change, and the
  carrier sometimes gives no estimate.

  PASS if REQUIREMENTS, RISKS or TEST SCENARIOS says, in any wording, that
  the tracking service must handle a `parcel.dispatched` message that
  carries no `estimated_delivery` (an older message, one from a pod not yet
  rolled, one where the carrier gave no estimate) without failing — showing
  nothing or a placeholder for the estimate — with a stated behaviour or a
  test scenario for a message without the field.
  FAIL if the reply never addresses a message without the field reaching
  the tracking service, or assumes every message now carries it.
weight: 1
---

Keeps the one real requirement of an additive field: the reader that will
show it copes with the messages that do not carry it.
