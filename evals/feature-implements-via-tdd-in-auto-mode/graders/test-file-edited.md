---
type: tool_used
tool: Edit
input_match: "stats.test.js"
min: 1
max: 999
weight: 1
---

The Red step must add the new tests to the existing test file rather than
inventing a separate one. Matches an `Edit` call on `test/stats.test.js`; if
the agent instead rewrites the file with `Write`, this grader under-counts —
see the eval's caveats.
