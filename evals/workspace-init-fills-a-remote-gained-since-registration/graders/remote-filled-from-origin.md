---
type: regex
target:
  source: file
  path: roadmap/repos.md
pattern: "\\|\\s*orders-api\\s*\\|\\s*active\\s*\\|\\s*REST backend owning the `orders` domain\\s*\\|\\s*git@example\\.com:acme/orders-api\\.git\\s*\\|"
flags: ""
match: contains
weight: 3
---

`orders-api` gained an `origin` since it was registered with `—`: the
Remote cell now carries that URL, and the row's status and role are
unchanged around it.
