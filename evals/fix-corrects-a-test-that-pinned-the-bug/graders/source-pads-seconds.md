---
type: llm
focus: { source: file, path: "src/duration.js" }
criteria: |
  PASS if `formatDuration` writes the seconds with two digits for every
  input — a leading zero below 10 (`padStart(2, "0")`, a conditional "0"
  prefix, `slice(-2)`, or an equivalent) — so 65 gives "1:05" and 125
  gives "2:05".
  FAIL if the seconds are still written as a bare number, or if only some
  values are special-cased (65, or 125 kept as "2:5").
weight: 3
---

The root cause is fixed in the formatter, for every value.
