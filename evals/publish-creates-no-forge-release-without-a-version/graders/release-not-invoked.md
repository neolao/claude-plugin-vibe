---
type: tool_used
tool: Skill
input_match: "\"skill\"\\s*:\\s*\"(?:[\\w-]+:)?release\""
min: 0
max: 0
weight: 2
---

`## [Unreleased]` is empty: nothing to release, so `vibe:release` must not
run.
