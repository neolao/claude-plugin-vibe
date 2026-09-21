---
type: tool_used
tool: Agent
input_match: "vibe:review-architecture"
min: 0
max: 0
weight: 1
---

`review-architecture` is only active when `.vibe/` exists. This fixture has no
`.vibe/` directory, so it must not be launched. Precision matters as much as
recall here: a review that fires every agent regardless of the project isn't
actually reading Step 1's activation table.
