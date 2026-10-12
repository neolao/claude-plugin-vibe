---
type: regex
target: trace
pattern: 'git rm[^"\n]*001'
weight: 2
---

The file is removed with `git rm`, as Step 3 prescribes, and not left behind or deleted with plain `rm`.
