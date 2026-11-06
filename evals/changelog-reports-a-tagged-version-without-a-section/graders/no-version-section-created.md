---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "^## "
flags: m
match: count:2
weight: 2
---

Exactly two `## ` headings, `[Unreleased]` and `[1.0.0]`: the missing
`[1.1.0]` section is reported, not written — cutting a version is
`vibe:release`'s job.
