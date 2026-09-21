---
type: tool_used
tool: Bash
input_match: "unittest|pytest"
min: 1
max: 999
weight: 1
---

review-tests is the one review agent that executes rather than only reads:
it must actually attempt the suite command before grounding its findings in
the result. A run that fails (missing pytest, missing driver) still counts —
not attempting it at all does not.
