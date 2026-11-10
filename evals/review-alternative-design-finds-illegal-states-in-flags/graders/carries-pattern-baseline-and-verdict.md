---
type: regex
target: last_message
pattern: "PATTERN[*_]*:[\\s\\S]*?BASELINE[*_]*:[\\s\\S]*?VERDICT[*_]*:[\\s*_]*BETTER[\\s*_]*\\(?[^\\n)]{0,20}\\d"
flags: i
weight: 1
---

At least one finding carries the agent's own three extra lines in order —
`PATTERN:`, `BASELINE:` and `VERDICT: BETTER (won/lost)` with a count (`5/7`, `won 5, lost 2`, `5 won`) — so
the classifier can re-check the baseline and the score, not only the idea.
Markdown emphasis around a label still matches.
