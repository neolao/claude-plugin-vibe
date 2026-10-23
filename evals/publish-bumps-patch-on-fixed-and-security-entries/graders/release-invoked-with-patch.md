---
type: tool_used
tool: Skill
input_match: "(?=.*\"skill\"\\s*:\\s*\"(?:[\\w-]+:)?release\")(?=.*patch)"
min: 1
max: 999
weight: 2
---

Step 2 decides the bump itself: Fixed and Security entries neither add
nor alter behaviour, so the bump is patch, passed explicitly to
`vibe:release`.
