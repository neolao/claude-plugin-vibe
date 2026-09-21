---
type: tool_used
tool: Skill
input_match: "\"skill\"\\s*:\\s*\"vibe:fix\""
min: 1
max: 999
weight: 2
---

The item's title/description use defect vocabulary ("crash"), so Step 7
should classify it as a fix and hand off to `vibe:fix`, never to
`vibe:feature`.
