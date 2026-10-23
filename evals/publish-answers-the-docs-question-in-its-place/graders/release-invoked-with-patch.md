---
type: tool_used
tool: Skill
input_match: "(?=.*\"skill\"\\s*:\\s*\"(?:[\\w-]+:)?release\")(?=.*patch)"
min: 1
max: 999
weight: 1
---

Step 2 still runs: the Fixed-only `## [Unreleased]` section gives a patch
bump, passed explicitly to `vibe:release`.
