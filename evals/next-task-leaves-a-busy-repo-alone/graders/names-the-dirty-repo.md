---
type: llm
focus: last_message
criteria: |
  billing-api has an uncommitted edit in `src/main.py`.

  PASS if the message says billing-api was left out of this run because
  its working tree has uncommitted changes (or words to that effect:
  dirty, not clean, local changes).
  FAIL if billing-api is not mentioned, or is left out for another reason,
  or its item is offered as a candidate or runner-up.
weight: 2
---

Names the repo with uncommitted work and why it was left out.
