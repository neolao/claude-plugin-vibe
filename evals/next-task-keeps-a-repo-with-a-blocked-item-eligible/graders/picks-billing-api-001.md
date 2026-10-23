---
type: llm
focus: last_message
criteria: |
  billing-web 003's notes wait on billing-api#001, so billing-api 001
  unblocks one item; billing-web 001 unblocks none. billing-api's working
  tree is clean and its item 002 is `blocked`, not `in_progress`.

  PASS if the presented pick is item 001 in billing-api.
  FAIL if it picks billing-web 001, billing-api 002, or reports no
  candidate.
weight: 3
---

Picks the unblocking item of a clean repo that also holds a blocked item.
