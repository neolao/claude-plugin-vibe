---
type: llm
focus: trace
criteria: |
  The skill supports exactly two tracking paths and must be explicit about
  which one it took: `TaskCreate` when the dedicated task system exists in
  the environment, or — when it does not — saying so out loud and writing a
  `task-list.md` checklist to the scratchpad directory instead.

  PASS if the response states unambiguously which of the two paths was used,
  and that statement matches what actually happened in the run (tasks created
  through the task system, or a scratchpad checklist written after announcing
  the fallback).
  FAIL if the response is silent about how the list was tracked, or claims
  one path while the run shows the other — in particular, claiming the task
  system was used when no task was ever created, which is the exact failure
  the skill's fallback wording exists to prevent.
weight: 1
---

States which of the two tracking paths it took, truthfully. Replaces the
former pair of path-specific graders, which were mutually exclusive by
construction and kept the case's ceiling below 1.00.
