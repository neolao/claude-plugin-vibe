---
type: tool_used
tool: Skill
input_match: "\"skill\"\\s*:\\s*\"(?:[\\w-]+:)?docs\""
min: 1
max: 999
weight: 2
---

`docs/architecture.md` carries the `vibe:docs` banner, so Step 4 invokes
`vibe:docs` to refresh it for the new version.
