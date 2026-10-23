---
type: regex
target: { source: file, path: README.md }
pattern: "TODO: fill in features"
match: not_contains
flags: i
weight: 1
---

The features section was rewritten: the fixture's placeholder sentence
does not survive.
