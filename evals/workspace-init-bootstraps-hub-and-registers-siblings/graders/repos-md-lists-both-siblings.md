---
type: regex
target:
  source: file
  path: roadmap/repos.md
pattern: "(?=.*\\|\\s*orders-api\\s*\\|\\s*active\\s*\\|)(?=.*\\|\\s*orders-sdk\\s*\\|\\s*planned\\s*\\|)"
flags: s
match: contains
weight: 2
---

`repos.md`'s table lists both siblings with the correct status each should
get: `orders-api` auto-classified `active` (it already has `.vibe/backlog/`),
`orders-sdk` `planned` (it has no `.vibe/`, so its status had to be asked
rather than guessed).
