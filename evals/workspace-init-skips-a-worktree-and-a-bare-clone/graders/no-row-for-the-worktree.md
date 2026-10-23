---
type: regex
target:
  source: file
  path: roadmap/repos.md
pattern: "\\|\\s*orders-api-hotfix\\s*\\|"
flags: ""
match: not_contains
weight: 2
---

`orders-api-hotfix` is a linked worktree of `orders-api` (its `.git` is a
file): a second checkout of a repo already registered, never a sibling
of its own.
