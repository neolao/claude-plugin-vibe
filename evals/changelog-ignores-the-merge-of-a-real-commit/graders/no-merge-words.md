---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "(Merge pull request|#12|alice)"
flags: i
match: not_contains
weight: 1
---

The merge boilerplate stays out of the file.
