---
type: regex
target: last_message
pattern: "CLARIFY-RESULT:\\s*settled[\\s\\S]*?### Synthesis"
weight: 1
---

Once every question is answered decisively, the run must end with the
skill's exact `CLARIFY-RESULT: settled` line followed by a `### Synthesis`
section, per Step 5 of the skill's contract.
