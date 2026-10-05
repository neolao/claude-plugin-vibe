---
type: regex
pattern: '\[Unreleased\]: https://github\.com/example/fixture-app/compare/v1\.11\.0\.\.\.HEAD[\s\S]*\[1\.11\.0\]: https://github\.com/example/fixture-app/compare/v1\.10\.0\.\.\.v1\.11\.0'
target: { source: file, path: "CHANGELOG.md" }
match: contains
weight: 2
---

Compare links are updated: `[Unreleased]` now compares from v1.11.0 and `[1.11.0]` compares v1.10.0 to v1.11.0.
