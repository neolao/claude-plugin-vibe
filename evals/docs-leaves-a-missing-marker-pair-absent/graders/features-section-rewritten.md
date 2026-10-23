---
type: regex
target: { source: file, path: README.md }
pattern: "TODO: fill in features"
match: not_contains
flags: i
weight: 1
---

The pairs that are present are still rewritten: a missing pair does not
turn the whole README into a hand-written one.
