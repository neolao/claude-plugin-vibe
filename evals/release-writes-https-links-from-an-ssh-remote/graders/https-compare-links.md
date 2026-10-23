---
type: regex
pattern: '\[Unreleased\]: https://github\.com/example/fixture-app/compare/v1\.2\.4\.\.\.HEAD[\s\S]*\[1\.2\.4\]: https://github\.com/example/fixture-app/compare/v1\.2\.3\.\.\.v1\.2\.4'
target: { source: file, path: "CHANGELOG.md" }
match: contains
weight: 3
---

The links are https compare links in the file's own form: `[Unreleased]`
now compares from v1.2.4, `[1.2.4]` compares v1.2.3 to v1.2.4 — the SSH
remote was rewritten as `https://github.com/example/fixture-app`.
