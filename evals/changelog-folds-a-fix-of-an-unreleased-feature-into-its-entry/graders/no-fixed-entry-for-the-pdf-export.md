---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "### Fixed(?:(?!\\n##)[\\s\\S])*PDF"
match: not_contains
weight: 3
---

No `### Fixed` section mentions the PDF export: its crash was fixed before
any release shipped it, so no user of a released version ever met it.
