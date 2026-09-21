---
type: tool_used
tool: TaskCreate
min: 3
max: 999
weight: 0.5
---

When the dedicated task system is available in the sandbox, `TaskCreate`
should be called at least three times (one per task). Given a lower weight
because this path is only one of the two the skill explicitly supports —
see `creates-chain-tolerant-of-either-path.md` for the path-agnostic check.
