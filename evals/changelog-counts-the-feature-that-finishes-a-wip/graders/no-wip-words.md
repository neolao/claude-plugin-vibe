---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "(\\bwip\\b|plan rejected|partial|unfinished)"
flags: i
match: not_contains
weight: 1
---

The wip commit's own vocabulary stays out of the file: the entry describes
the export the user gets, not the history of how it landed.
