---
type: regex
pattern: '## \[Unreleased\]\s*## \[1\.2\.4\] - \d{4}-\d{2}-\d{2}[\s\S]*Fix crash when loading a config file with no entries\.[\s\S]*## \[1\.2\.3\] - 2026-01-15'
target: { source: file, path: "CHANGELOG.md" }
match: contains
weight: 2
---

The absence of a remote changes nothing else: the section is cut at
`[1.2.4]` under a fresh `[Unreleased]`, `[1.2.3]` untouched below.
