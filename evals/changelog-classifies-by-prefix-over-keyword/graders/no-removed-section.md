---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "### Removed"
match: not_contains
weight: 1
---

No feature was taken away. The word `remove` in a fix's subject must not
open a `### Removed` section.
