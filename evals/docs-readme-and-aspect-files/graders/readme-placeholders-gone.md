---
type: regex
target: { source: file, path: README.md }
pattern: "TODO: (fill in features|document install steps|document usage examples|fill in the documentation index)"
match: not_contains
flags: i
weight: 1
---

Every managed section (features, install, usage, docs-index) was rewritten —
none of the stale placeholder sentences from the fixture survive.
