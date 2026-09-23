---
type: tool_used
tool: Bash
input_match: "gh\\s+run\\s+(list|view)"
min: 1
max: 999
weight: 2
---

Step 3 must actually query the workflow run (via the fixture's `gh` stand-in
documented in its `CLAUDE.md`), not just claim a result in prose.
