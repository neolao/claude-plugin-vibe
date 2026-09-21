---
type: llm
focus: last_message
criteria: |
  In fixtures/export_writer.py, `export_orders` writes inside a `with`
  block so the handle closes even if a write raises, and
  `load_export_template` re-raises with `raise ... from e`, preserving the
  original cause and naming the failing `path` in the message.

  PASS if no `high` or `medium` severity finding claims either function
  leaks a file handle or loses the error's cause or identifier.
  FAIL if either is flagged as a Resource or Lost context issue (or
  equivalent) at high or medium severity.
weight: 1
---

Does not flag the `with`-guarded write or the cause-preserving rethrow.
