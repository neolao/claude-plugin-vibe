---
type: llm
focus: last_message
criteria: |
  A `blocked` item is one an autonomous run gave up on; nobody is working
  on it. billing-api's tree is clean.

  PASS if the message does not say billing-api was left out, skipped or
  unavailable for this run, and does not describe it as having work in
  progress or uncommitted changes (it may mention item 002 as blocked and
  not a candidate).
  FAIL if billing-api is reported as left out of the run, busy, dirty, or
  as holding an item in progress.
weight: 2
---

A blocked item does not make its repo busy.
