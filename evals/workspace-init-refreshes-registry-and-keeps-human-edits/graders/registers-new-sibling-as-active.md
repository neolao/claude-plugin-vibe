---
type: regex
target:
  source: file
  path: roadmap/repos.md
pattern: "\\|\\s*orders-web\\s*\\|\\s*active\\s*\\|"
flags: ""
match: contains
weight: 1
---

`orders-web` is a new sibling with `.vibe/backlog/`: it is registered as
`active` without being asked.
