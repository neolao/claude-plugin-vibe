---
type: llm
focus: last_message
criteria: |
  The agent's definition never rates unneeded machinery `high`: it is a
  cost, not a bug.

  PASS if no reported finding carries SEVERITY `high`. A report with no
  findings at all passes.
  FAIL if any finding carries SEVERITY `high`.
weight: 1
---

No finding at `high`, whatever the category.
