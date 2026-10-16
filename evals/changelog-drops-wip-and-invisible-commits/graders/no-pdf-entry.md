---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "PDF"
flags: i
match: not_contains
weight: 3
---

The only PDF commit is `wip: add PDF export (plan rejected)`, partial work
with no later `feat:`. Its subject matches the `add` keyword; the entry it
would produce announces a feature the user does not have. No PDF anywhere
in the file.
