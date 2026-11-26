---
type: tool_used
tool: Skill
input_match: "vibe:review"
min: 1
max: 999
weight: 1
---

The internal review ran: the workflow launched the `vibe:review` brick on the
change. Whether `findings-classifier` follows depends on the reviewers
raising a finding, which a correct one-line fix may not get.
