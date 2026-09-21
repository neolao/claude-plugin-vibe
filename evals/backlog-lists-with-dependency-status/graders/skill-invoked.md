---
type: tool_used
tool: Skill
input_match: "\"skill\"\\s*:\\s*\"(?:[\\w-]+:)?backlog\""
min: 1
max: 999
weight: 1
---

Sanity check: the `vibe:backlog` skill was actually invoked, rather than the
top-level session listing the files itself.
