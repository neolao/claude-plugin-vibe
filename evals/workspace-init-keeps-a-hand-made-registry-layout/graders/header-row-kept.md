---
type: regex
target:
  source: file
  path: roadmap/repos.md
pattern: "\\|\\s*Repo\\s*\\|\\s*Path\\s*\\|\\s*Status\\s*\\|\\s*Role\\s*\\|\\s*Owner\\s*\\|"
flags: ""
match: contains
weight: 2
---

The hand-made header row, with its `Path` and `Owner` columns, is still
the table's header: the file was edited, not rewritten to the
four-column template.
