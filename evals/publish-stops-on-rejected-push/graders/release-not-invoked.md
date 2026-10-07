---
type: tool_used
tool: Skill
input_match: "\"skill\"\\s*:\\s*\"(?:[\\w-]+:)?release\""
min: 0
max: 0
weight: 2
---

Step 1 failing stops the whole skill: `vibe:release` must not run, although
the changelog holds a releasable `### Fixed` entry.
