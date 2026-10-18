---
type: tool_used
tool: Skill
input_match: "\"skill\"\\s*:\\s*\"(?:[\\w-]+:)?report\""
min: 2
max: 999
weight: 1
---

Sanity check: `vibe:report` was invoked at least twice (`init`, then
`write`), rather than the session running the script from memory.
