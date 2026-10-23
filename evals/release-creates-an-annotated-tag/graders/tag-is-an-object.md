---
type: regex
pattern: 'tag\|v1\.2\.4'
target: last_message
match: contains
weight: 3
---

`git for-each-ref refs/tags/v1.2.4 --format='%(objecttype)|%(contents:subject)'`
prints `tag|v1.2.4` for an annotated tag whose subject is the version; a
lightweight tag prints `commit|chore: release v1.2.4` instead.
