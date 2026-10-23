---
type: tool_used
tool: Skill
input_match: "(?=.*\"skill\"\\s*:\\s*\"(?:[\\w-]+:)?release\")(?=.*minor)"
min: 1
max: 999
weight: 2
---

Step 2 decides the bump itself: a `## [Unreleased]` section holding only a
`### Changed` entry is altered behaviour, a minor bump, passed explicitly
to `vibe:release`.
