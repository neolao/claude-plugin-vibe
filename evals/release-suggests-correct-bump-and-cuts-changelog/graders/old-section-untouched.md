---
type: regex
pattern: '## \[1\.2\.3\] - 2026-01-15\n\n### Fixed\n\n- Fix off-by-one error in the pagination component\.\n\n\[Unreleased\]:'
target: { source: file, path: "CHANGELOG.md" }
match: contains
weight: 2
---

The previously released `## [1.2.3]` section is left byte-for-byte
unchanged, right down to the blank line before the compare links — the
skill only ever rewrites `[Unreleased]` and inserts new sections above it.
