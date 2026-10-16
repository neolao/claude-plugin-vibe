---
type: llm
focus: last_message
criteria: |
  The brief says the broker redelivers a message when the consumer that took
  it dies before acknowledging it. A replica killed between the provider
  accepting the email and the acknowledgement means another replica sends
  the same confirmation again.

  PASS if REQUIREMENTS, RISKS, or TEST SCENARIOS ties redelivery to the
  requirement that the same `order.paid` message does not send the email
  twice, and says how: an idempotency key or deduplication by order or
  message id on the provider call, a sent marker recorded before
  acknowledging, or an equivalent — not a generic "add retries with backoff".
  FAIL if duplicate emails from a redelivered message are not addressed, or
  only generic retry advice is given without the idempotency angle.
weight: 2
---

Ties the broker's redelivery to idempotent sending, so a redelivered message
does not email the customer twice.
