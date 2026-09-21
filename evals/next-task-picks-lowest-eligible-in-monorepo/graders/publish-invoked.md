---
type: tool_used
tool: Skill
input_match: "\"skill\"\\s*:\\s*\"vibe:publish\""
min: 1
max: 999
weight: 1
---

`vibe:next-task` must invoke `vibe:publish` after the fix, whatever
`vibe:fix` reported, so that everything committed locally reaches the
remote (or fails trying).
