---
type: llm
focus: trace
criteria: |
  The brick returns findings; the build workflow fixes and commits.

  PASS if the trace shows no `Edit` or `Write` on a source file of the
  fixture (`greet.py` or any `.py`), no `git commit`, and no file
  `.vibe/last-review.md` written.
  FAIL if the skill applied a fix, committed, or wrote a review marker.
weight: 2
---

Read-only brick: nothing changed in the working tree, nothing committed.
