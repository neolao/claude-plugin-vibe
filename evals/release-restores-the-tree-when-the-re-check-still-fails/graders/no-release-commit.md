---
type: regex
pattern: 'chore: release v1\.2\.4'
target: last_message
match: not_contains
weight: 2
---

`git log --oneline -3` shows no release commit: the skill stopped before
Step 7.
