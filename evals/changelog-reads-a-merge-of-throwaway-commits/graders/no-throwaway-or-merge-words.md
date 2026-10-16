---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "(\\bwip\\b|fixup|typo|Merge pull request|#12|alice)"
flags: i
match: not_contains
weight: 2
---

Neither the throwaway subjects nor the merge boilerplate belongs in the
file: the entry is the export the user gets.
