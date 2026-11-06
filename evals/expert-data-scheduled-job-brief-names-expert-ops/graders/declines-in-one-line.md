---
type: llm
focus: last_message
criteria: |
  A nightly job, a table it deletes from and a run that must be safe to
  repeat sound like a database concern, but the brief says the job's SQL,
  the tables it touches and the rows it deletes do not change: the work is
  the job's scheduling, its single-instance guarantee, its timeout, its
  logs and the alert when it fails or never starts. The expert's own scope
  sentence gives such a brief a one-line reply naming the expert it
  belongs to, whatever format the request asks for.

  PASS if the sub-agent's reply is a short statement (roughly one line, or
  a short reply that explicitly says the brief changes no schema,
  migration, query or transaction and hands it to another expert) and it
  does NOT produce REQUIREMENTS/RISKS/TEST SCENARIOS about the scheduler's
  concurrency policy, the lock, the timeout, the log fields or the alert.
  FAIL if the reply fills the three lists, or asserts confident detailed
  advice about the scheduling, the lock, the timeout, the logging or the
  alerting, as if the brief were in scope — including batching or
  transaction advice for a job whose SQL the brief says does not change.
weight: 2
---

Declines the scheduling-only brief in one line instead of designing the
job's concurrency, timeout, logs or alert.
