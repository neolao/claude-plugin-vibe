---
type: tool_used
tool: Bash
input_match: "chore: auto run"
min: 0
max: 0
weight: 2
---

A new run that starts no item is never opened or closed: neither a
`chore: auto run — start NNN` nor a `chore: auto run — 0 items …` commit may
be made, so a `/loop` firing on a drained backlog leaves the history alone.
