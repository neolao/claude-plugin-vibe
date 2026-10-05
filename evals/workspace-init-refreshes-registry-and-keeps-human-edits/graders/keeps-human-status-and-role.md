---
type: regex
target:
  source: file
  path: roadmap/repos.md
pattern: "\\|\\s*orders-api\\s*\\|\\s*planned\\s*\\|\\s*Billing gateway, owned by the payments squad\\s*\\|"
flags: ""
match: contains
weight: 2
---

`orders-api` was already listed: its `planned` status and its hand-written
role are kept exactly as they were, never overwritten by a re-scan.
