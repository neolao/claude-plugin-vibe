---
type: llm
focus: last_message
criteria: |
  In fixtures/export_writer.py, `export_orders` writes to a `.tmp` file
  inside a `with` block (the handle closes even if a write raises), moves it
  into place with `os.replace` only after every row is written, and deletes
  the temp file before re-raising on failure (any `OSError` from that
  cleanup is suppressed, so the original exception is the one raised) — no
  partial export and no stray temp file is left behind. `load_export_template` re-raises with
  `raise ... from e`, preserving the original cause and naming the failing
  `path` in the message.

  PASS if no `high` or `medium` severity finding claims either function
  leaks a file handle, leaves partial or temp state behind on failure, or
  loses the error's cause or identifier.
  FAIL if either is flagged as a Resource or Lost context issue (or
  equivalent) at high or medium severity.
weight: 1
---

Does not flag the atomic, cleaned-up write or the cause-preserving rethrow.
