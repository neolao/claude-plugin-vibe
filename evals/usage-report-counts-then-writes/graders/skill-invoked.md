---
type: tool_used
tool: Skill
input_match: "\"skill\"\\s*:\\s*\"(?:[\\w-]+:)?usage-report\""
min: 1
max: 999
weight: 1
---

Sanity check: `vibe:usage-report` was invoked (at the latest for `init`),
rather than the session running the script from memory. The `write` invocation
is not required: the skill's text is already loaded after `init`.
