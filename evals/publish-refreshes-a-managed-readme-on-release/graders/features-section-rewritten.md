---
type: regex
target: { source: file, path: README.md }
pattern: "TODO: fill in features"
match: not_contains
flags: i
weight: 2
---

The managed Features section is rewritten by the release's docs refresh:
a README with markers is managed, nothing about it is declined or left
as it was.
