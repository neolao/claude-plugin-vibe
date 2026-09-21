---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "(Merge branch|bump deps|lodash|formatting tweak|tidy|entry point|wip)"
flags: i
match: not_contains
weight: 2
---

The refactor, the dependency bump, the merge commit and the incidental
formatting commit it carries are all invisible to users and must produce no
entry — the same noise rule as the recall twin, checked here where there is
no real entry to hide behind.
