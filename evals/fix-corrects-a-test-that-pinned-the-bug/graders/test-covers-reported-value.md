---
type: regex
target:
  source: file
  path: test/duration.test.js
pattern: "\\b65\\b[\\s\\S]{0,40}?[\"'`]1:05[\"'`]"
weight: 1
---

The reproducing test exists: the reported value, 65 seconds, reads "1:05".
