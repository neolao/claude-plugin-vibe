---
type: regex
target: last_message
pattern: "SUITE EXECUTED:[\\s\\S]*E2E/INTEGRATION EXECUTED:"
flags: i
weight: 1
---

The agent's own contract opens every report with
`SUITE EXECUTED: [command] → PASS/FAIL (...)` followed by
`E2E/INTEGRATION EXECUTED: yes/no — [command, or why it could not run]`.
