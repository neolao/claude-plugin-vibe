---
type: regex
pattern: '\]: https?://|/compare/|/releases/tag/'
target: { source: file, path: "CHANGELOG.md" }
match: not_contains
weight: 3
---

No link was added: the repo has no remote, so there is no base URL, and a
URL guessed from the package name would be an invention.
