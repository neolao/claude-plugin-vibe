---
type: llm
focus: trace
criteria: |
  Look at the task operations recorded in the trace (calls to `tasks.sh`
  through Bash, `TaskUpdate`/`TaskCreate`, or edits of a `tasks.tsv` file).

  PASS if, at the moment of the return to planning:
  - exactly the `pending` tasks were deleted (here only "Commit"), through
    `tasks.sh … abandon` or one `deleted` transition per pending task;
  - no task already `completed` ("Plan", "Implement") was deleted, reopened
    or re-created in place; "Review" was completed, never deleted;
  - the new round's tasks were created afterwards with subjects prefixed
    `Round 2 — ` and chained by their dependencies.
  FAIL if a completed task was deleted or edited back to pending, if the
  whole list was wiped and rebuilt, if "Commit" stayed pending, or if the
  second round's tasks were created without the prefix.
weight: 2
---

Checks the mechanics of going back on the task store itself, not only the
status lines: completed tasks are the trace of the previous round and stay.
