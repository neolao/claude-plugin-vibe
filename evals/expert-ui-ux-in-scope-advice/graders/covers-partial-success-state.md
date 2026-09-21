---
type: llm
focus: last_message
criteria: |
  PASS if the reply names a distinct "partial success" outcome for this
  import — some rows created, some rejected — as its own state to design for
  (not folded silently into a plain "success" or "error" state), e.g. a
  requirement or test scenario about a mixed-result screen listing which rows
  succeeded/failed after upload.
  FAIL if the reply only mentions all-succeed and all-fail outcomes, or a
  generic "handle errors" statement with no explicit partial/mixed-result
  case for this CSV import.
weight: 2
---

Explicitly calls out the partial-success (some rows in, some rows rejected)
outcome as a state of its own for this import, not just success/error.
