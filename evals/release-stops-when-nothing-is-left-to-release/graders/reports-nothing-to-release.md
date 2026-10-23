---
type: llm
focus: last_message
criteria: |
  The changelog refresh found only a CI housekeeping commit since the last
  tag and left `[Unreleased]` empty, so the skill stops: there is nothing
  to release.

  PASS if the final report says that no release was made because there
  was nothing to release — an empty Unreleased section, no user-visible
  change since the last tag, or equivalent wording — and names no new
  version as released.
  FAIL if the report claims a version was released or tagged, invents a
  changelog entry for the CI change, or gives a different reason for
  stopping (a failing check, a dirty tree).
weight: 2
---

Confirms the stop is explained as "nothing to release", not as a failure.
