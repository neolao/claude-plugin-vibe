---
type: tool_used
tool: Bash
input_match: "feat:"
min: 1
max: 999
weight: 1
---

The Commit step must land a `feat:`-prefixed commit once tests are green —
checked as a `git commit` invocation whose message contains `feat:`.
