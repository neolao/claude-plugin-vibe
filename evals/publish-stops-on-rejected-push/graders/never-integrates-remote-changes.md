---
type: tool_used
tool: Bash
input_match: "git\\s+(pull|rebase|merge)"
min: 0
max: 0
weight: 1
---

The skill stops at a rejected push and hands the blocker to the user. It does
not improvise a pull, rebase or merge to get around it.
