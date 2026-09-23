---
type: regex
pattern: '"version":\s*"1\.2\.3"'
target: { source: file, path: "package.json" }
match: contains
weight: 1
---

`package.json`'s `version` field must stay at `1.2.3` — Step 5 (bump the
version) must never run once the build has failed.
