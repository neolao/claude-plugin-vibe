---
type: tool_used
tool: Bash
input_match: "npm test|node --test"
min: 1
max: 999
weight: 1
---

The runner is configured in `fixtures/package.json`, above the path under
review: the agent must still find and execute it rather than conclude from
the scope alone that there is nothing to run.
