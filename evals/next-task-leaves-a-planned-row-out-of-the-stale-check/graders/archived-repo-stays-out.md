---
type: llm
focus: last_message
criteria: |
  legacy-batch is listed `archived` in repos.md and its directory is still
  in the workspace, with a backlog item that two billing-api items wait on.
  Only `active` repos supply candidates, and a sibling scan never changes a
  registered row's status.

  PASS if the presentation never offers a legacy-batch item as the pick or
  as a runner-up (it may name it as the reason billing-api 002 and 003 are
  blocked).
  FAIL if a legacy-batch item is presented as a candidate, pick or
  runner-up.
weight: 2
---

Leaves the archived repo out, although its directory and backlog exist.
