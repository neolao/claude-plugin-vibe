---
type: regex
pattern: '## \[Unreleased\]\s*## \[0\.5\.0\] - \d{4}-\d{2}-\d{2}[\s\S]*Add a CSV export for monthly reports\.'
target: { source: file, path: "CHANGELOG.md" }
match: contains
weight: 2
---

The changelog is cut at `[0.5.0]` with the pending Added entry, under a
fresh `[Unreleased]`.
