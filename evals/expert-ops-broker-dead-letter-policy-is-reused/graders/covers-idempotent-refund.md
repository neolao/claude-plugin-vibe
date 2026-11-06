---
type: llm
focus: last_message
criteria: |
  The broker redelivers a message when the consumer that took it dies
  before acknowledging it, and the provider accepts a client reference on
  each refund call. A replica killed after the provider accepted the refund
  but before the acknowledgement means another attempt refunds the same
  order again.

  PASS if REQUIREMENTS, RISKS or TEST SCENARIOS ties redelivery to the
  requirement that the same `refund.requested` message refunds the
  customer once, and says how: the order id or message id as the
  provider's client reference so a second call is recognised, a refunded
  marker checked before calling, or an equivalent — and that the message
  is acknowledged only after the provider has accepted the refund (or
  after the order is marked), not on receipt.
  FAIL if a redelivered message refunding twice is not addressed, or only
  generic retry advice is given without the client reference or an
  equivalent idempotency angle, or when the message is acknowledged is
  never addressed.
weight: 2
---

Ties the broker's redelivery to the provider's client reference and an
acknowledgement after the refund is accepted, so no customer is refunded
twice.
