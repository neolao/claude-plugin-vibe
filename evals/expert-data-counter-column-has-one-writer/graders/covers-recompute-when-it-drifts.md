---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS, RISKS or TEST SCENARIOS provides a way to
  recompute `comment_count` from the comments when it is wrong — a rebuild
  query or a batched job that resets every task's count from `COUNT(*)` —
  and settles the initial value for the existing tasks (computed from
  their comments when the column is added, in batches on the large table,
  rather than defaulting to zero and staying wrong).
  FAIL if the reply has no way to repair a drifted count, or adds the
  column with a default of zero for the existing tasks with no word on
  computing their real count.
weight: 2
---

Provides the recompute path — the initial fill from the existing comments
and a rebuild when the count drifts — instead of a column that is right
only while nothing goes wrong.
