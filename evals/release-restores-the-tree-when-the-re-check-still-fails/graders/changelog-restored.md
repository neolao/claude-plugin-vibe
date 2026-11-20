---
type: regex
pattern: '## \[Unreleased\]\s*\n\s*### Fixed\s*\n\s*- Fix crash when loading a config file with no entries\.\s*\n\s*## \[1\.2\.3\]'
target: { source: file, path: "CHANGELOG.md" }
match: contains
weight: 2
---

The changelog cut of Step 3 is undone: the pending entry is back under
`[Unreleased]`, with no `[1.2.4]` section between it and `[1.2.3]`.
