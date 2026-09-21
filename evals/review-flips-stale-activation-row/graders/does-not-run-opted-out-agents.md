---
type: tool_used
tool: Agent
input_match: "vibe:review-(tests|security)\\b"
min: 0
max: 0
weight: 1
---

Neither deliberately opted-out agent may be launched. `review-web-security`
is matched by its own grader and the word boundary keeps it out of this one.
