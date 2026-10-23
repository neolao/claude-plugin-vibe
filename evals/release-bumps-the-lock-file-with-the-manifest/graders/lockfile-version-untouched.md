---
type: regex
pattern: '"lockfileVersion":\s*3'
target: { source: file, path: "package-lock.json" }
match: contains
weight: 1
---

`lockfileVersion` is npm's format version, not the project's: it stays 3.
