---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "(code quality|vibe:review|single page|\\btests?\\b|\\bwip\\b|plan rejected)"
flags: i
match: not_contains
weight: 2
---

The `refactor:` renames a loop variable and the `test:` adds a test:
nothing the user can observe, whatever the prefix says. Neither produces
an entry, and the wip's own words do not leak into the file either.
