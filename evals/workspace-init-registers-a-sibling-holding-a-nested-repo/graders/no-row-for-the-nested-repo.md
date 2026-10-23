---
type: regex
target:
  source: file
  path: roadmap/repos.md
pattern: "\\|\\s*(pricing-lib|vendor|orders-api/vendor/pricing-lib)\\s*\\|"
flags: ""
match: not_contains
weight: 2
---

`vendor/pricing-lib` is a repo nested inside `orders-api`: nothing is
scanned below a sibling, so it gets no row of its own.
