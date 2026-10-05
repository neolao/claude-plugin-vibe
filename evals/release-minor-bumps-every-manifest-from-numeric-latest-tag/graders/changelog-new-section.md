---
type: regex
pattern: '## \[Unreleased\]\s*## \[1\.11\.0\] - \d{4}-\d{2}-\d{2}[\s\S]*Add a CSV export for monthly reports\.[\s\S]*## \[1\.10\.0\] - 2026-03-02'
target: { source: file, path: "CHANGELOG.md" }
match: contains
weight: 2
---

A fresh empty `[Unreleased]` sits above a dated `[1.11.0]` section holding the pending entry, and `[1.10.0]` is untouched below.
