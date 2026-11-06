---
type: llm
focus: last_message
criteria: |
  The brief adds one optional filter flag and one optional output switch
  and changes nothing that exists: the unchanged invocation prints the same
  columns in the same order and `--older-than` is untouched. The expert's
  own checklist says an added flag that leaves the defaults alone needs no
  transition.

  PASS if no REQUIREMENTS entry demands a deprecation period, a
  deprecation warning, an alias for an existing flag, a version bump of the
  CLI, a notice to the other teams or a migration of their scripts as a
  condition of this change. Stating that the unchanged invocation keeps
  printing what it did, with a test scenario for it, is expected and
  passes; a RISKS entry noting that a script might still break on an
  unexpected table change also passes.
  FAIL if REQUIREMENTS requires a deprecation cycle, an alias, a version
  bump, a migration of the other teams' scripts or their prior agreement
  as the condition for adding `--status` or `--json`.
weight: 2
---

Does not reach for a transition on an additive change: the compatibility
rule triggers on what existing scripts would feel, and here they feel
nothing.
