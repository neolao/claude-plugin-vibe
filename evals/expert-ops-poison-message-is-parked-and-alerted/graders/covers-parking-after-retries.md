---
type: llm
focus: last_message
criteria: |
  The brief recounts a message the consumer could not parse being rejected
  and redelivered at the head of the queue every few milliseconds for a
  weekend, with every message behind it waiting and nobody looking. The
  expert's own checklist settles what happens to a message that still
  fails after its retries: it is parked and alerted on, never redelivered
  forever ahead of the rest and never dropped silently.

  PASS if REQUIREMENTS, RISKS or TEST SCENARIOS requires, for this
  consumer, that a message still failing after a bounded number of
  attempts is moved aside — a dead-letter queue or exchange, a parking
  table, a quarantine — so the queue keeps moving, and that this parking
  raises an alert someone receives, with a stated behaviour or a test
  scenario for an unparseable message (it ends up parked, the next message
  is processed, someone is told).
  FAIL if the reply never raises what happens to a message that fails
  every attempt, prescribes only "retries with backoff" with no end
  state, has the consumer discard an unparseable message with only a log
  line, or raises parking only as an `OPEN QUESTIONS:` entry asking the
  Product Owner whether or how to handle it.
weight: 2
---

Requires a message that keeps failing to be parked with an alert so the
queue keeps moving, as a requirement and not an open question.
