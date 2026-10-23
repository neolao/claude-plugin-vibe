---
type: tool_used
tool: Skill
input_match: "\"skill\"\\s*:\\s*\"(?:[\\w-]+:)?docs\""
min: 0
max: 0
weight: 3
---

No file in `docs/` carries the `vibe:docs` banner and the README has no
marker: Step 4 has nothing to refresh and must skip `vibe:docs` — a
`docs/` folder existing is not the condition.
