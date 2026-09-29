---
type: llm
focus: last_message
criteria: |
  workflow.md's Refactor and lint step re-runs the build command detected at
  baseline and treats a failure exactly like a failing test: diagnose, fix
  the code, re-run, before the task can reach Commit.

  PASS if the final report shows that the build command was run again after
  implementing the new function, that the project's build contract (the
  contract file the build checks) was brought up to date for the new
  function — whether the agent found the requirement from a failing build or
  from reading the build script beforehand — and that the build was
  confirmed passing before the work was committed.
  FAIL if the report never mentions the build after implementation, shows a
  build failure being ignored or worked around (for example by editing the
  build script), or shows the commit happening before the build was
  confirmed green.
weight: 2
---

Confirms, from the reported narrative, that the build gate was exercised
and the contract requirement was met for real rather than skipped or
bypassed. Accepts both paths (failure caught then fixed, or requirement
anticipated), since the agent reads the small project's build script while
exploring.
