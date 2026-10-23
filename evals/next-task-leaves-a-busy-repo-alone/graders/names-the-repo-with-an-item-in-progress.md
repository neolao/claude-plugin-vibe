---
type: llm
focus: last_message
criteria: |
  billing-jobs holds item 001 at `status: in_progress`.

  PASS if the message says billing-jobs was left out of this run because
  one of its items is in progress (another session, or an interrupted
  run), and does not offer billing-jobs 002 as a candidate or runner-up.
  FAIL if billing-jobs is not mentioned, is left out for another reason,
  or one of its items is offered as a candidate or runner-up.
weight: 2
---

Names the repo with an item in progress and why it was left out.
