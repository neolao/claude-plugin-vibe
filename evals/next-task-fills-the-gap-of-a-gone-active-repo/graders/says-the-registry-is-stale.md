---
type: llm
focus: last_message
criteria: |
  The registry lists legacy-batch as active while its directory is gone,
  and does not list billing-jobs. Step 2 fills the gap for this run and
  mentions it.

  PASS if the message says the registry is stale, out of date or in need of
  a refresh, or names at least one of the two discrepancies: legacy-batch
  missing from the workspace, or billing-jobs not listed in repos.md.
  FAIL if the message says nothing about either discrepancy.
weight: 2
---

Reports the stale registry instead of silently working around it.
