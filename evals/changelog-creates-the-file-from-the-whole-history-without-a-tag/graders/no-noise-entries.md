---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "(bump deps|lodash|initial commit)"
flags: i
match: not_contains
weight: 1
---

The initial commit and the dependency bump are noise, in a whole-history
read as in a tagged one.
