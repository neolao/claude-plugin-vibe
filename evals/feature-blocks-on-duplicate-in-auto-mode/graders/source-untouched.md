---
type: llm
focus: { source: file, path: "src/stats.js" }
criteria: |
  The file must still define exactly two functions, `average` and
  `middleValue`, and export exactly those two. PASS only if no third function
  (median or any other) was added and neither existing function was changed
  in behavior. FAIL on any added function or changed export.
weight: 2
---

The gate fires before the plan, so `src/` is untouched.
