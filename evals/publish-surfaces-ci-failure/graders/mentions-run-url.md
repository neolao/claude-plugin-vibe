---
type: regex
target: last_message
pattern: "actions/runs/555111000"
weight: 2
---

Deterministic check on the report text: the actual run URL from the mocked
`gh` output must appear, proving the report is grounded in the real query
result rather than a generic, made-up blocker message.
