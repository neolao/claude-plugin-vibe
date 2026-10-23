---
type: regex
target:
  source: file
  path: roadmap/repos.md
pattern: "(?=.*\\|\\s*orders-api\\s*\\|\\s*active\\s*\\|)(?=.*\\|\\s*orders-web\\s*\\|\\s*active\\s*\\|)"
flags: s
match: contains
weight: 2
---

Both plain siblings have `.vibe/backlog/`, so both are registered as
`active` — the nested repo inside `orders-api` does not disqualify it.
