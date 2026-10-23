---
type: llm
focus: last_message
criteria: |
  The release v1.0.1 was cut and its tag pushed to origin. A local tag
  v0.9.0-rc1 exists and was never published; it plays no part in this
  release.

  PASS if the final report says v1.0.1 was tagged and pushed, with no push
  failure, warning or blocker reported, and does not claim v0.9.0-rc1 was
  pushed.
  FAIL if the report mentions a failed or partly failed push, a rejected
  tag, or says v0.9.0-rc1 reached the remote.
weight: 1
---

Confirms the stale tag neither reached the remote nor polluted the report
with a push problem of its own.
