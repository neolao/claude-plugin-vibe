---
type: regex
pattern: '"version":\s*"1\.2\.3"'
target: { source: file, path: "package.json" }
match: contains
weight: 1
---

`package.json` stays at `1.2.3`: nothing was written.
