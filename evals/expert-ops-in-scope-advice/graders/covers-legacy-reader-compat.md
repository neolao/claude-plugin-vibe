---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS, RISKS or TEST SCENARIOS flags that the legacy
  nightly reporting job reads the same `events` table the new worker
  writes into, and that what the worker writes (new rows, new columns,
  changed shape or semantics) must keep that job working. Naming the job
  and the shared table together is what counts; tying it to the rolling
  deploy is not required.
  FAIL if the legacy reporting job is not mentioned as a reader that must
  keep working, or only appears in passing (e.g. "totals unaffected" in a
  duplicate-delivery test) with no compatibility concern of its own.
weight: 2
---

Flags that the legacy nightly reporting job, reading the same `events`
table, must keep working on what the new worker writes.
