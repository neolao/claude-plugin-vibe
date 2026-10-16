---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*### Added(?:(?!\\n## \\[)[\\s\\S])*### Fixed"
weight: 1
---

The fix was committed before the feature, but Keep a Changelog orders
categories Added, Changed, Deprecated, Removed, Fixed, Security — the
table's order, not the commit order.
