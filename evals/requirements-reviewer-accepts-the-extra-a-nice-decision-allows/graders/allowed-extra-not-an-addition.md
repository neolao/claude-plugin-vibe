---
type: llm
focus: last_message
criteria: |
  The framing's fourth decision, "**Moved ids** (✨ NICE): the run may also
  keep the ids of the moved rows in `ledger.last_moved_ids`", covers the
  `last_moved_ids` attribute and its assignment in fixtures/archive.py;
  the third decision covers the `dry_run` parameter and its early return.
  Both are delivered as the framing allows.

  PASS if no `(addition)` finding targets `last_moved_ids`, `dry_run`, or
  the tests that exercise them.
  FAIL if either is reported as an addition.
weight: 2
---

An extra the framing explicitly allows is covered by a requirement.
