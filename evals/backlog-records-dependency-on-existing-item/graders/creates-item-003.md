---
type: regex
target: files
pattern: "^\\.vibe/backlog/003-[a-z0-9-]+\\.md$"
flags: m
match: "count:1"
weight: 1
---

Exactly one new item is created, numbered `003` (the fixture holds `001` and
`002`, no `done/`), per Step 6.
