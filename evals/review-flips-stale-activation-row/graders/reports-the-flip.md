---
type: llm
focus: last_message
criteria: |
  Step 1 requires every flipped row to be listed in the `## REVIEW flipped
  rows` section of the output; the caller commits the updated `CLAUDE.md`.

  PASS if the final report names `review-web-security` as a row it flipped
  from inactive to active, and says why (the project does expose HTTP
  routes).
  FAIL if the report never mentions the activation-table change, or mentions
  it without naming which row changed.
weight: 1
---

Surfaces the activation-table change in the report instead of changing the
table silently.
