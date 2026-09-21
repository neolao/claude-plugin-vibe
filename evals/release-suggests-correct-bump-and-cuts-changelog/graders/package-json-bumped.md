---
type: regex
pattern: '"version":\s*"1\.2\.4"'
target: { source: file, path: "package.json" }
match: contains
weight: 1
---

`package.json`'s `version` field was bumped from `1.2.3` to `1.2.4` (Step 5
of the skill, run against every project manifest).
