---
type: llm
focus: { source: file, path: ".vibe/auto-state.md" }
criteria: |
  When the run was interrupted, `current: 002` was in flight; the item is in
  fact already at `.vibe/backlog/done/002-add-first-of.md`, so Step 0's
  "finished after all" row applies: journal it `done` and move on.

  PASS if the journal's line for item 002 now records a `done` verdict rather
  than leaving it in progress, and `current:` no longer names 002.
  FAIL if 002 is re-run, marked blocked, or left in flight.
weight: 2
---

Resumes by journaling the already-finished 002 as done instead of re-running
it.
