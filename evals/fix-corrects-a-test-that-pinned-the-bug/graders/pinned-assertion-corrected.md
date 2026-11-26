---
type: regex
target:
  source: file
  path: test/duration.test.js
pattern: "[\"'`]2:5[\"'`]"
match: not_contains
weight: 3
---

The existing assertion that 125 seconds reads "2:5" asserted the reported
defect. The fix corrects it ("2:05") instead of keeping it green.
