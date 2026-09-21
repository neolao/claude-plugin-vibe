---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "### Added[\\s\\S]{0,500}(CSV|csv)"
weight: 1
---

The `feat: add CSV export for monthly reports` commit lands under `### Added`
in `[Unreleased]`.
