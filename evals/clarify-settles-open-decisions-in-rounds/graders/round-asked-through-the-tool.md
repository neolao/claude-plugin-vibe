---
type: regex
target: trace
pattern: "\"name\":\\s*\"AskUserQuestion\"|\"query\":\\s*\"[^\"]*AskUserQuestion"
weight: 1
---

The open product decisions are asked through `AskUserQuestion`: a round
written as text at the end of a turn is easy to miss. `claude plugin eval`
never offers the tool (it is absent from the session's tool list even with
`--allow-tools AskUserQuestion`), so the grader checks that the run reaches
for it — a call to it, or a `ToolSearch` loading it — before falling back
to the text round. The pattern matches tool-use JSON only, not the skill
text quoting the tool's name.
