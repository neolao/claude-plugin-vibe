---
type: llm
focus: last_message
criteria: |
  billing-api is the only `active` repo. Its items 002 and 003 wait on
  legacy-batch#001 in their notes, and legacy-batch is `archived`, so
  billing-api 001 is the only unblocked candidate.

  PASS if the presented pick is item 001 in billing-api.
  FAIL if it picks any other item, in billing-api or elsewhere.
weight: 3
---

Picks the only unblocked candidate of the only active repo.
