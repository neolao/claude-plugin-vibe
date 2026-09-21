---
type: regex
target: last_message
pattern: "CLARIFY-RESULT:\\s*abandoned"
match: contains
weight: 2
---

Declining Round 1 outright, with nothing settled, must yield the exact
`CLARIFY-RESULT: abandoned` line from Step 5 of the skill's contract —
not `settled` or `partial`.
