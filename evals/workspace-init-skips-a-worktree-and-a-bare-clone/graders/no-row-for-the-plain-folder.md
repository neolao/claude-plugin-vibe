---
type: regex
target:
  source: file
  path: roadmap/repos.md
pattern: "\\|\\s*notes\\s*\\|"
flags: ""
match: not_contains
weight: 1
---

`notes/` has no `.git` at all: ignored, not registered.
