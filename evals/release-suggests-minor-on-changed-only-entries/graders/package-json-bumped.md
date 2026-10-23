---
type: regex
pattern: '"version":\s*"1\.3\.0"'
target: { source: file, path: "package.json" }
match: contains
weight: 1
---

`package.json` carries version 1.3.0.
