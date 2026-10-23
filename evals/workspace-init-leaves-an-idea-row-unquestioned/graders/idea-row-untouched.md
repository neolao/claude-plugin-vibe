---
type: regex
target:
  source: file
  path: roadmap/repos.md
pattern: "\\|\\s*orders-sdk\\s*\\|\\s*idea\\s*\\|\\s*Shared TypeScript client, no repo yet\\s*\\|"
flags: ""
match: contains
weight: 3
---

`orders-sdk` is an `idea`: no directory is expected, so the row is kept
exactly as written. Had the skill raised the remove-or-archive question,
the pre-answered "remove it" would have taken the row out.
