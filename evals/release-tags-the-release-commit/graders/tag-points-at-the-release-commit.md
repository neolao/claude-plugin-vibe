---
type: regex
pattern: 'target\|chore: release v1\.2\.4'
target: last_message
match: contains
weight: 3
---

`git log -1 --format='target|%s' v1.2.4^{commit}` prints the subject of
the commit the tag points at: it must be the release commit, not the
initial commit the fixture tagged v1.2.3.
