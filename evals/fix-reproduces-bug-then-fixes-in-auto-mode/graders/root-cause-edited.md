---
type: tool_used
tool: Edit
input_match: "list-utils.js"
min: 1
max: 999
weight: 2
---

The fix must change the actual root cause (the `max` implementation's wrong
accumulator initialization in `src/list-utils.js`), not just add a test.
Matches an `Edit` call on the source file; if the agent instead rewrites it
with `Write`, this grader under-counts — see the eval's caveats. The
`input_match` string is `list-utils.js`, which does not appear as a
contiguous substring in `list-utils.test.js`, so the two files are not
conflated.
