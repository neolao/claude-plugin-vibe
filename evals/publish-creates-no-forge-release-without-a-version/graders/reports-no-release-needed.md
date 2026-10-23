---
type: llm
focus: last_message
criteria: |
  The local commit was pushed; `## [Unreleased]` is empty, so no release
  was cut and no GitHub release had to be created.

  PASS if the final report says the push succeeded and that no release
  was needed (or equivalent: nothing to release, changelog empty), with
  the forge release reported as skipped or not applicable (or not
  mentioned at all) and no blocker.
  FAIL if the report says a version was tagged or pushed, says a GitHub
  release was created, or raises a blocker about the push.
weight: 1
---

Confirms a run with nothing to release announces nothing on the forge.
