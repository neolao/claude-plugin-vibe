---
type: regex
target: last_message
pattern: "AUTO-RESULT:\\s*blocked[^\\n]*duplicate"
weight: 2
---

An already-covered capability in `--auto` mode resolves to
`AUTO-RESULT: blocked — possible duplicate of ...`, never `done`: the caller
moves on to the next item instead of shipping the same feature twice.
