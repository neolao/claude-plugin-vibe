---
type: regex
pattern: '## \[1\.2\.4\] - \d{4}-\d{2}-\d{2}[\s\S]*### Fixed[\s\S]*Fix crash when loading a config file with no entries\.[\s\S]*Fix incorrect timestamp formatting in the export log\.'
target: { source: file, path: "CHANGELOG.md" }
match: contains
weight: 2
---

`CHANGELOG.md` now has a dated `## [1.2.4]` section carrying the two `Fixed`
entries that were pending under `[Unreleased]` (Step 3).
