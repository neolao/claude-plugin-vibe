---
type: llm
focus: last_message
criteria: |
  The fixture's workflow runs on manual dispatch only, so the pushed
  commit triggered no run and the `gh` stand-in lists none. Step 3 of
  vibe:publish waits a bounded time for a run to appear, then treats CI
  as not observable and moves on — nothing depends on it.

  PASS if the final report says no workflow run was found or triggered
  for the commit (CI not observable, nothing to poll, or equivalent),
  with no blocker, warning or concern raised about it, and does not claim
  CI is green, failed, or still running.
  FAIL if the report claims a run succeeded, failed or is still running
  after the poll limit, raises any blocker about CI, or says the run
  gave up because of a timeout of the whole skill.
weight: 3
---

Confirms the absence of a run is reported as "not observable" rather than
as a result that never existed, and that the step did not hang.
