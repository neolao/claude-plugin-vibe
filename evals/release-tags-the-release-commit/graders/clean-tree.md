---
type: regex
pattern: 'porcelain-lines\|0'
target: last_message
match: contains
weight: 1
---

`printf 'porcelain-lines|%s\n' "$(git status --porcelain | wc -l | tr -d ' ')"`
prints `porcelain-lines|0`: nothing the steps changed was left out of the
release commit.
