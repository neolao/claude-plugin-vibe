---
type: regex
pattern: '"version":\s*"1\.2\.3"'
target: { source: file, path: "package.json" }
match: contains
weight: 1
---

`package.json`'s `version` field stays at `1.2.3`: Step 5 never runs when
the skill stops on an empty section.
