---
type: llm
focus: last_message
criteria: |
  Nothing else in the fixture breaks S, L, or the remaining principles: each
  type has one reason to change and no subtype narrows its base's contract.

  PASS if no `high` or `medium` severity `S` or `L` finding is reported on
  this code.
  FAIL if any is.
weight: 1
---

Reports no residual SRP or LSP violation on sound code.
