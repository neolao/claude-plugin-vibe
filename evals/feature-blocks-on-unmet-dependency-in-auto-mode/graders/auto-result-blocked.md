---
type: regex
target: last_message
pattern: "AUTO-RESULT:\\s*blocked"
weight: 2
---

`/vibe:auto` relies on this line and nothing else: an unmet dependency in
`--auto` mode resolves to `AUTO-RESULT: blocked`, never `done` or `aborted`.
