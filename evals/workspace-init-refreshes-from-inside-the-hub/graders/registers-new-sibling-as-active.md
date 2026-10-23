---
type: regex
target:
  source: file
  path: roadmap/repos.md
pattern: "\\|\\s*orders-web\\s*\\|\\s*active\\s*\\|"
flags: ""
match: contains
weight: 2
---

Run from inside the hub, the skill still scans the hub's parent folder:
`orders-web`, a new sibling with `.vibe/backlog/`, is registered as
`active`.
