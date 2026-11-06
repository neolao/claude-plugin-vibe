---
type: llm
focus: last_message
criteria: |
  The brief says nobody looks at the consumer once it is live, the bus
  keeps undelivered messages for seven days, and the consumer needs bus
  and database credentials no service holds today. A consumer that stops
  (crashed, credentials rejected, database unreachable) archives nothing,
  and the gap is found when accounting looks for an invoice, possibly
  years later.

  PASS if REQUIREMENTS, RISKS or TEST SCENARIOS requires that a consumer
  that stops consuming is noticed without someone reading logs — an alert
  on the queue's depth or its oldest message, on the consumer's absence or
  on its last successful write, a readiness or liveness signal wired to
  the platform's alerting, or an equivalent — and that the process refuses
  to start without its new credentials (or fails fast when they are
  missing).
  FAIL if the only observability asked for is logging, or if a stopped
  consumer reaching nobody is never raised, or if the new credentials'
  absence at startup is never addressed.
weight: 2
---

Requires a stopped consumer to be alerted on and the new credentials to
fail fast when missing: an archive nobody watches must not fail silently
for years.
