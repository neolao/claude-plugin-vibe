---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "(typo|README)"
flags: i
match: not_contains
weight: 1
---

`Fix typo in README` matches the `fix` keyword but changes nothing the
user of the library observes: noise, no entry.
