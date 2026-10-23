---
type: llm
focus: last_message
criteria: |
  billing-jobs is not in repos.md but is a sibling with `.git/` and a
  backlog, so the skill adds it for this run. billing-api 002's notes wait
  on billing-jobs#001, so billing-jobs 001 unblocks one item and billing-api
  001 unblocks none.

  PASS if the presented pick is item 001 in billing-jobs.
  FAIL if it picks billing-api 001, any other item, or reports no
  candidate at all.
weight: 3
---

Takes the unlisted sibling into account and picks its unblocking item.
