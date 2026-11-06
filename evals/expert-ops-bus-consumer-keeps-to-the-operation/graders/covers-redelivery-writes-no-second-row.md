---
type: llm
focus: last_message
criteria: |
  The broker redelivers a message when the consumer dies before
  acknowledging it: a replica killed after the archive row is committed but
  before the acknowledgement means the same `invoice.issued` message is
  handled again.

  PASS if REQUIREMENTS, RISKS or TEST SCENARIOS ties redelivery to the
  requirement that the same invoice is archived once, and says how: the
  message acknowledged only after the row is committed, and the write made
  idempotent on the invoice id (an upsert, an insert that ignores an
  existing invoice id, a uniqueness the write relies on) — not a generic
  "add retries with backoff".
  FAIL if a redelivered message producing a second archive row is not
  addressed, or only generic retry advice is given without the idempotency
  angle.
weight: 2
---

Ties the broker's redelivery to acknowledging after the commit and an
idempotent write, so a redelivered message archives no invoice twice.
