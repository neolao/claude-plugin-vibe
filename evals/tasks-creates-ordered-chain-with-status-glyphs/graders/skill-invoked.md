---
type: tool_used
tool: Skill
input_match: "\"skill\"\\s*:\\s*\"(?:[\\w-]+:)?tasks\""
min: 1
max: 999
weight: 1
---

Sanity check: the `vibe:tasks` skill was actually invoked, rather than the
top-level session tracking progress on its own.
