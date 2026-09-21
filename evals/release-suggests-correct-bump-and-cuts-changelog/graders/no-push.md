---
type: tool_used
tool: Bash
input_match: 'git push'
min: 0
max: 0
weight: 1
---

Nothing was pushed. `/vibe:release` is local-only by design — `vibe:publish`
(via `/vibe:auto --push` or `/vibe:next-task`) or the user pushes separately.
