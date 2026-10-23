---
type: tool_used
tool: Bash
input_match: "gh\\s+(run\\s+(list|view)|api)"
min: 1
max: 999
weight: 1
---

Step 3 must actually look for the workflow run (via the fixture's `gh`
stand-in documented in its `CLAUDE.md`), not decide from the workflow file
alone.
