---
type: regex
pattern: '## \[Unreleased\]\s*## \[1\.3\.0\] - \d{4}-\d{2}-\d{2}[\s\S]*### Added[\s\S]*CSV export[\s\S]*### Fixed[\s\S]*Fix crash when loading a config file with no entries\.[\s\S]*## \[1\.2\.3\] - 2026-01-15'
target: { source: file, path: "CHANGELOG.md" }
match: contains
weight: 2
---

The cut `[1.3.0]` section carries both the Added entry the refresh wrote
from the `feat:` commit and the Fixed entry that was already pending, under
a fresh empty `[Unreleased]`, with `[1.2.3]` untouched below.
