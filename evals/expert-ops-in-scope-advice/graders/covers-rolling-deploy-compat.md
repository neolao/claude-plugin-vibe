---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS or RISKS flags that the new worker writes into the
  `events` table that the existing legacy nightly reporting job also
  reads, and that this must survive a rolling deploy (old and new
  containers/consumers coexisting, or the legacy job reading rows the new
  worker wrote) without breaking the reporting job — a concrete
  compatibility concern, not a generic "test before deploying" statement.
  FAIL if the shared-table / rolling-deploy compatibility risk with the
  legacy reporting job is absent or only stated generically.
weight: 2
---

Flags the rolling-deploy compatibility risk between the new worker's writes
and the legacy reporting job reading the same `events` table.
