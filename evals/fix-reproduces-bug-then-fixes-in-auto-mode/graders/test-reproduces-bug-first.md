---
type: tool_used
tool: Bash
input_match: "npm test"
min: 2
max: 999
weight: 2
---

The workflow itself runs the test suite at least twice in its own context: the
baseline check, and the confirmation re-run after the implementer returns (the
red and green runs happen inside the implementer, whose tool calls are not in
the trace). The Refactor re-run usually makes a third.
