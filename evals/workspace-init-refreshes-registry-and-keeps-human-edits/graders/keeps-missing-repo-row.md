---
type: regex
target:
  source: file
  path: roadmap/repos.md
pattern: "\\|\\s*legacy-portal\\s*\\|"
flags: ""
match: contains
weight: 1
---

`legacy-portal` is listed but has no directory in the workspace. The answer
to the removal question is "keep it", so its row stays.
