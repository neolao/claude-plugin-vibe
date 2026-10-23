---
type: regex
pattern: '"version":\s*"0\.5\.0"'
target: { source: file, path: "package.json" }
match: contains
weight: 1
---

`package.json` carries version 0.5.0.
