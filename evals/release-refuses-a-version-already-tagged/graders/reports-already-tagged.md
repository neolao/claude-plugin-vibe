---
type: llm
focus: last_message
criteria: |
  PASS if the final report says no release was made because version
  1.2.3 (tag v1.2.3) already exists / is already tagged, and claims no
  file change, commit or tag.
  FAIL if the report claims a release, a commit or a tag was made, gives
  another reason for stopping, or says the skill went through the
  changelog cut or the version bump before stopping.
weight: 2
---

Confirms the stop happened for the stated reason and before any write.
