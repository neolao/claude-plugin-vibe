---
type: file_exists
path: "**/task-list.md"
exists: true
weight: 0.5
---

When the dedicated task system is unavailable in the sandbox, the skill's
documented fallback is a `task-list.md` scratchpad checklist. Given a lower
weight because this path is only one of the two the skill explicitly
supports — see `creates-chain-tolerant-of-either-path.md` for the
path-agnostic check.
