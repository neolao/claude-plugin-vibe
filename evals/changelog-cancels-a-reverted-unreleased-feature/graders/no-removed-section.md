---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "### Removed"
match: not_contains
weight: 2
---

Nothing the user had was taken away — the PDF export was never released.
The revert cancels the feature; it is not a removal to announce.
