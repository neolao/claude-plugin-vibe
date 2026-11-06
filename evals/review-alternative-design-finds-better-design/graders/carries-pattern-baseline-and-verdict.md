---
type: regex
target: last_message
pattern: "PATTERN[*_]*:[\\s\\S]*?BASELINE[*_]*:[\\s\\S]*?VERDICT[*_]*:[\\s*_]*BETTER[\\s*_]*\\(?\\s*\\d+\\s*(/|won|,)"
flags: i
weight: 1
---

At least one finding carries the agent's own three extra lines in order —
`PATTERN:`, `BASELINE:` and `VERDICT: BETTER (won/lost)` with a count — so
the classifier can re-check the baseline and the score, not only the idea.
Markdown emphasis around a label still matches.
