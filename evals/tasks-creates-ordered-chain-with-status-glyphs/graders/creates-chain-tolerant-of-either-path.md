---
type: llm
focus: trace
criteria: |
  PASS if a 3-item task chain matching "Write tests" (no dependency),
  "Implement" (blocked by "Write tests"), and "Commit" (blocked by
  "Implement") was recorded, by either of these two paths — either is
  acceptable, since the skill explicitly supports both:
  - the dedicated task system: three `TaskCreate` calls with `addBlockedBy`
    chaining Implement after Write tests and Commit after Implement, or
  - the documented fallback: a `task-list.md` checklist (`- [ ] <subject>`)
    in the same order, announced explicitly as a fallback because the
    dedicated task system was unavailable.
  FAIL if fewer than three tasks were recorded, if the dependency chain is
  wrong or missing, or if neither path was used (e.g. progress was only
  narrated in chat with no task system and no checklist file).
weight: 2
---

Confirms the ordered dependency chain was actually created, tolerant of
which of the skill's two documented mechanisms handled it.
