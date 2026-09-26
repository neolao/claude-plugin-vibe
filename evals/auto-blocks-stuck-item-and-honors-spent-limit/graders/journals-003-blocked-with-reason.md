---
type: llm
focus: { source: file, path: ".vibe/auto-state.md" }
criteria: |
  Item 003 was `current` at `attempt: 2` when the run was interrupted. On
  resume the attempt count goes above 2, so the skill gives up on it.

  PASS if the journal's line for item 003 records a `blocked` verdict with a
  reason saying it failed to resume after an interruption (or an equivalent
  wording about repeated resume attempts).
  FAIL if 003's line still reads in progress, records `done`, or records
  `blocked` with no reason.
weight: 2
---

Journals the stuck item as blocked, with the resume-cap reason.
