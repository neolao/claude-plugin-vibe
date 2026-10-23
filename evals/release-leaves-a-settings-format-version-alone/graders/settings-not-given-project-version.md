---
type: regex
pattern: '1\.2\.[34]'
target: { source: file, path: "config/settings.json" }
match: not_contains
weight: 2
---

Neither the old nor the new project version was written into the
settings file.
