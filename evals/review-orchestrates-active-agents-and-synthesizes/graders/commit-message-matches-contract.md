---
type: regex
target: trace
pattern: "(refactor: apply code quality fixes from vibe:review|chore: record vibe:review run)"
weight: 1
---

Step 6 specifies the exact commit subject for each case: `refactor: apply
code quality fixes from vibe:review` if any high/medium fix was applied
(the hardcoded-secret finding is a very plausible one to auto-fix), otherwise
`chore: record vibe:review run`. Either is acceptable; a made-up message is
not.
