---
type: regex
target: { source: file, path: README.md }
pattern: "Tiny-pub-lib started as a weekend exercise in publishing a package by hand; this paragraph is maintained entirely by hand and must never be rewritten by any tooling, no matter what else changes in this file\\."
match: contains
weight: 1
---

The hand-written README paragraph survives byte-for-byte.
