---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "(Merge branch|bump deps|lodash|formatting tweak|wip)"
flags: i
match: not_contains
weight: 2
---

The merge commit (`Merge branch 'topic' into main`), the incidental
`chore: wip formatting tweak` commit brought in by that merge, and the
`chore: bump deps` commit are all noise and must produce no changelog entry.
