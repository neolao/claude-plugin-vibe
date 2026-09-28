---
type: regex
target: { source: file, path: README.md }
pattern: "Widgetcli grew out of a team hack day; the maintainers keep this paragraph by hand to explain where the project came from, and no generator is allowed to reword it\\."
match: contains
weight: 2
---

The hand-written README paragraph outside the managed markers survives
byte-for-byte.
