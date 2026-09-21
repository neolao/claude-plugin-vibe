---
type: tool_used
tool: Skill
input_match: "(?=.*\"skill\"\\s*:\\s*\"(?:[\\w-]+:)?release\")(?=.*patch)"
min: 1
max: 999
weight: 2
---

`vibe:publish` (Step 2) must decide the bump itself from the Fixed-only
`## [Unreleased]` section (patch) and invoke `vibe:release` with that word
explicit — the skill's own rule is "always explicit, never blank".
