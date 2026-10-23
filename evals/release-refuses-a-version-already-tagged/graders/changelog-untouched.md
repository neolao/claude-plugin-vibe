---
type: regex
pattern: '## \[Unreleased\]\s*\n\s*### Fixed\s*\n\s*- Fix crash when loading a config file with no entries\.\s*\n\s*## \[1\.2\.3\] - 2026-01-15'
target: { source: file, path: "CHANGELOG.md" }
match: contains
weight: 2
---

`[Unreleased]` still carries its pending entry directly above `[1.2.3]`:
no section was cut for a version that already exists.
