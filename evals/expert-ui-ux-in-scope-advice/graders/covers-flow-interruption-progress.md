---
type: llm
focus: last_message
criteria: |
  PASS if the reply addresses the multi-second validation delay and/or the
  admin navigating away or closing the tab mid-import — e.g. a requirement
  for visible progress during the check, and/or a requirement that leaving
  mid-import doesn't lose the uploaded file or silently drop the import (no
  dead end, state preserved or the import continues/resumes).
  FAIL if the reply never addresses progress feedback during the multi-second
  check, and never addresses what happens if the admin leaves before it
  finishes.
weight: 2
---

Addresses either visible progress during the multi-second validation, or
what happens if the admin leaves mid-import, tied to this CSV import.
