---
type: llm
focus: last_message
criteria: |
  legacy-batch's Status column says `archived`; the word "active" appears
  only in its Role text. Its directory is still in the workspace, with a
  backlog item that two billing-api items wait on. Only repos whose Status
  is `active` supply candidates.

  PASS if the presentation never offers a legacy-batch item as the pick or
  as a runner-up (it may name it as the reason billing-api 002 and 003 are
  blocked).
  FAIL if a legacy-batch item is presented as a candidate, pick or
  runner-up.
weight: 3
---

Takes the status from the Status column, not from the row's other text.
