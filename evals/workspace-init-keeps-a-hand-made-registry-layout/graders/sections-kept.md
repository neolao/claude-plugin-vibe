---
type: regex
target:
  source: file
  path: roadmap/repos.md
pattern: "(?=.*Every repo is prefixed with the product name: `orders-<component>`\\.)(?=.*## Ownership)(?=.*Each squad owns the repos listed with its name in the Owner column)"
flags: s
match: contains
weight: 2
---

The written naming convention and the extra `## Ownership` section
survive the refresh word for word.
