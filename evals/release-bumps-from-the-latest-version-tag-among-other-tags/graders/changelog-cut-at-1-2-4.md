---
type: regex
pattern: '## \[Unreleased\]\s*## \[1\.2\.4\] - \d{4}-\d{2}-\d{2}[\s\S]*The tool no longer fails when the widget file is missing\.[\s\S]*## \[1\.2\.3\] - 2026-01-15'
target: { source: file, path: "CHANGELOG.md" }
match: contains
weight: 2
---

The changelog is cut at `[1.2.4]` with the pending Fixed entry, under a
fresh `[Unreleased]`, `[1.2.3]` untouched below.
