---
type: regex
pattern: 'porcelain-lines\|0'
target: last_message
match: contains
weight: 3
---

`git status --porcelain` of the enclosing repo (`orders-api`) prints no
line: no `roadmap/` or `CLAUDE.md` was written under `orders-api/src`,
which is what a run mistaking that subdirectory for the workspace root
leaves behind.
