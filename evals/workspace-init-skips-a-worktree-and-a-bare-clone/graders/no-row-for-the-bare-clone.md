---
type: regex
target:
  source: file
  path: roadmap/repos.md
pattern: "\\|\\s*mirror(\\.git)?\\s*\\|"
flags: ""
match: not_contains
weight: 2
---

`mirror.git` is a bare repository: no working tree to work in, so it
is not a sibling.
