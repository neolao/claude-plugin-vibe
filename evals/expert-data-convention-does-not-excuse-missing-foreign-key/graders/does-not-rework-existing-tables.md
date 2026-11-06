---
type: llm
focus: last_message
criteria: |
  The eleven existing tables have no foreign keys and store amounts as
  `double precision`, the app checks references itself, and the brief adds
  one table; nothing else changes. Adding foreign keys to tables that
  already hold orphaned rows, or converting their amount columns, is a
  separate migration with its own risks.

  PASS if no REQUIREMENTS entry makes adding foreign keys to the existing
  tables or converting their amount columns a non-negotiable of this
  change. The gap may be named in RISKS, as a later migration, or as advice
  for a future change: that passes.
  FAIL if REQUIREMENTS demands that the existing tables get foreign keys,
  that their `double precision` columns be converted, or that they be
  changed as part of this change.
weight: 1
---

Keeps the eleven existing tables out of this change's REQUIREMENTS:
consistency is restored by a named follow-up, not by a migration of
tables the brief does not touch.
