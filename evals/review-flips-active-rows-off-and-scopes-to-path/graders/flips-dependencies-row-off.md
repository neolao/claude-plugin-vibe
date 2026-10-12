---
type: regex
target: { source: file, path: "CLAUDE.md" }
pattern: "review-dependencies[^|]*\\|\\s*❌"
weight: 2
---

The reason says there is a dependency manifest while the project has none, so the row must now be marked inactive.
