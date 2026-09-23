---
type: llm
focus: last_message
criteria: |
  workflow.md's Refactor and lint step now re-runs the build command
  detected at baseline and treats a failure exactly like a failing test:
  diagnose, fix the code, re-run, before the task can reach Commit.

  PASS if the final report's narrative shows the build command was run
  again after implementing the new function, that it failed, that the
  agent diagnosed and fixed the real cause (not a workaround), and that it
  passed before the work was committed.
  FAIL if the narrative never mentions re-running the build after
  implementation, shows the build failure being ignored or worked around,
  or shows the commit happening before the build was confirmed green.
weight: 2
---

Confirms, from the reported narrative, that the build gate was exercised
for real and drove a genuine fix rather than being skipped or bypassed.
