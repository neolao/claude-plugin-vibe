---
type: llm
focus: trace
criteria: |
  Look only at the `TaskUpdate` calls the run made after "Review" was set
  `in_progress`.

  PASS if all of these hold:
  - "Review" was set `completed` before any task was set `deleted`;
  - exactly the two tasks still `pending` at that point ("Document" and
    "Commit") were each set to status `deleted` by a `TaskUpdate` call of
    their own, and the one with the lower id ("Document") was deleted
    before the other ("Commit");
  - no task among "Plan", "Implement" and "Review" was ever set `deleted`
    or set back to `pending`.
  FAIL if a pending task was left pending or never deleted, if the two
  deletions happened in the other order, if a completed task was deleted or
  reopened, or if the deletions happened before "Review" was completed.
weight: 2
---

In native mode there is no `drop-pending`: the skill asks for one `deleted`
transition per pending task, lowest id first, after the current task is
completed, and never touches a completed task.
