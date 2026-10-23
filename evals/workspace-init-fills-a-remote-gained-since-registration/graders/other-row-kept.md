---
type: regex
target:
  source: file
  path: roadmap/repos.md
pattern: "\\|\\s*orders-web\\s*\\|\\s*planned\\s*\\|\\s*Storefront web app, owned by the storefront squad\\s*\\|\\s*—\\s*\\|"
flags: ""
match: contains
weight: 2
---

`orders-web` has `.vibe/backlog/` but a human set it `planned`: the
status is kept, and so is its `—` Remote, since it has no origin.
