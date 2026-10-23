---
type: regex
pattern: '"version":\s*2,'
target: { source: file, path: "config/settings.json" }
match: contains
weight: 3
---

`config/settings.json` still says `"version": 2`: that is the settings
format version the code reads, not the project's version.
