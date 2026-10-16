---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "### Security"
match: not_contains
weight: 1
---

Nothing since the tag patches a vulnerability. The word `auth` in a
feature's subject must not open a `### Security` section.
