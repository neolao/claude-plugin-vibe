---
type: llm
focus: last_message
criteria: |
  The fixture's local branch is behind origin: a teammate pushed a commit the
  local branch does not have, so the push is rejected. Step 1 of vibe:publish
  stops there and reports the Git error as a blocker.

  PASS if the final report states the push was rejected or failed, gives the
  reason from Git (origin has commits the local branch lacks, non-fast-forward,
  fetch first), and presents it as something the user must resolve, without
  claiming the commit was pushed or a release was made.
  FAIL if it claims the push succeeded, says a release or tag was made, or
  mentions no push problem at all.
weight: 3
---

Confirms the rejected push is surfaced as a blocker rather than worked around
or hidden.
