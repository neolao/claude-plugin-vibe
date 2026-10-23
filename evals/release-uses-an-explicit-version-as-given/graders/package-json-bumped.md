---
type: regex
pattern: '"version":\s*"2\.0\.0"'
target: { source: file, path: "package.json" }
match: contains
weight: 1
---

`package.json` carries version 2.0.0.
