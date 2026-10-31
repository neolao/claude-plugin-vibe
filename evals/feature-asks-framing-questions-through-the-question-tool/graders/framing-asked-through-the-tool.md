---
type: regex
target: trace
pattern: "\"name\":\\s*\"AskUserQuestion\"|\"query\":\\s*\"[^\"]*AskUserQuestion"
weight: 3
---

The brief leaves open what counts as a large order and how much is taken
off; no file in the fixture says either. The need framing must ask, and a
question to the user goes through `AskUserQuestion`: a question written as
plain text at the end of a turn is easy to miss and gives no options to pick.

`claude plugin eval` never offers `AskUserQuestion` (not even with
`--allow-tools AskUserQuestion`: it is absent from the session's tool list),
so the grader checks that the run reaches for it — a call to it, or a
`ToolSearch` loading it — before falling back to a text round. The pattern
matches tool-use JSON only, not the skill text quoting the tool's name.
