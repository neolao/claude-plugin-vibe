---
type: tool_used
tool: Bash
input_match: "npm test"
min: 3
max: 999
weight: 2
---

The test suite must run at least three times: the baseline check, the red run
that proves the new test fails on the buggy code, and the green run after the
fix. Fewer runs mean the red or the green step was skipped. Together with
`red-before-green-order` (test edited before the source), this grades red
before green from the tool calls, since the final report is not required to
narrate the red step.
