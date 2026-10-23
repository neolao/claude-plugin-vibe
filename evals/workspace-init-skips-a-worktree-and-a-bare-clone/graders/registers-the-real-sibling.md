---
type: regex
target:
  source: file
  path: roadmap/repos.md
pattern: "\\|\\s*orders-api\\s*\\|\\s*active\\s*\\|"
flags: ""
match: contains
weight: 1
---

`orders-api`, the one real sibling (a `.git/` directory and
`.vibe/backlog/`), is registered as `active`.
