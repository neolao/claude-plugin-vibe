---
type: llm
focus: last_message
criteria: |
  The repo carries `vnext` and `deploy-2026-01-15` next to `v1.2.3`; the
  skill must bump from `v1.2.3`.

  PASS if the final report names 1.2.4 as the released version and gives
  1.2.3 (or `v1.2.3`) as the version it bumped from, or otherwise makes
  clear the non-version tags were set aside.
  FAIL if the report names any other released version, says it bumped
  from `vnext`, `deploy-2026-01-15` or `0.0.0`, or reports the release as
  blocked because the latest tag was not a version.
weight: 1
---

Confirms the base version was chosen deliberately, not recovered by
chance from the changelog.
