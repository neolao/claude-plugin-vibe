---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "^## "
flags: m
match: count:2
weight: 1
---

Exactly two `## ` headings: `[Unreleased]` and `[1.2.0]`. Neither
`deploy-2026-10-30` nor `vnext` is a version, and this skill never cuts
a version section anyway.
