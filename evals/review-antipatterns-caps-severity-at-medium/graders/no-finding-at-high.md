---
type: llm
focus: last_message
criteria: |
  The agent's definition never rates an anti-pattern `high`: an
  anti-pattern is a cost, not a bug.

  PASS if no reported finding carries SEVERITY `high`. A report with no
  findings at all passes.
  FAIL if any finding carries SEVERITY `high`.
weight: 1
---

No finding at `high`, whatever the category.
