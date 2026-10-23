---
type: llm
focus: last_message
criteria: |
  billing-api's working tree has an uncommitted change and billing-jobs
  holds an item at `status: in_progress`: Step 3 leaves both repos out of
  the run. billing-web is clean, and its item 001 is its only unblocked
  item (003 and 004 wait on the other repos).

  PASS if the presented pick is item 001 in billing-web.
  FAIL if it picks billing-api 001, billing-jobs 002, or any other item.
weight: 3
---

Picks from the one repo that is free to work in.
