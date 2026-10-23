---
type: tool_used
tool: Bash
input_match: "gh\\s+(run\\s+list|api)"
min: 3
max: 999
weight: 2
---

The stand-in lists the run only from the third listing on: fewer than
three listings means the step concluded "not observable" from an early
empty result instead of checking again within its bound.
