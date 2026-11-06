---
type: llm
focus: last_message
criteria: |
  The broker redelivers a message when the consumer that took it dies
  before acknowledging it. A consumer that acknowledges on receipt loses
  the update when it dies before writing it; one that acknowledges after
  the write sees the same message again when it dies between the write
  and the acknowledgement.

  PASS if REQUIREMENTS, RISKS or TEST SCENARIOS says, for this consumer,
  that a message is acknowledged only once the order change is written
  (committed) to the database, and that applying the same `order.updated`
  message twice leaves the order as if applied once — an idempotent
  update, a dedup on the message or event id, a version or timestamp
  check — with a stated behaviour or a test scenario for a consumer killed
  between the write and the acknowledgement.
  FAIL if when the message is acknowledged is never addressed, or if a
  redelivered message applying the change twice is never addressed.
weight: 2
---

Requires the acknowledgement after the change is written and an update
that a redelivery can apply twice without harm.
