---
type: tool_used
tool: Bash
input_match: "gh\\s+release\\s+create"
min: 0
max: 0
weight: 2
---

Step 4 runs only when a version was tagged: with nothing released,
`gh release create` must not be called, not even for the existing v1.0.0.
