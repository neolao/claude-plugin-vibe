---
type: tool_used
tool: Bash
input_match: "gh\\s+run\\s+(list|view)"
min: 0
max: 0
weight: 1
---

Step 3 must not attempt to query a workflow run at all once it has
established there is no workflow file — no `gh run list`/`gh run view`
call should appear, not even one that would predictably fail.
