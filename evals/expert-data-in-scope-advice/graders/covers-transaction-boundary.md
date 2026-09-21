---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS, RISKS, or TEST SCENARIOS names, tailored to this
  brief, that the inventory deduction and order insert must share one short
  database transaction, and that the external payment-gateway call must NOT
  sit inside that same transaction (an external call must not be made while
  holding a DB transaction open) — e.g. charge-then-record or a saga/outbox
  style split, so a slow/failed gateway call cannot block or corrupt the
  inventory+order write.
  FAIL if this transaction/external-call boundary is missing entirely, or
  only a generic "use transactions" remark not tied to the payment-gateway
  call in the brief.
weight: 2
---

Names the transaction boundary between the inventory/order write and the
external payment-gateway call as a concrete requirement or risk, tied to the
brief's checkout flow.
