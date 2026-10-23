---
type: regex
pattern: 'git@github\.com'
target: { source: file, path: "CHANGELOG.md" }
match: not_contains
weight: 2
---

The SSH form of the remote (`git@github.com:…`) never reaches the
changelog: a link built from it opens nowhere.
