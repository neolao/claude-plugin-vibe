---
type: llm
focus: last_message
criteria: |
  The other teams' scripts call `myctl backups list --older-than 30` and
  the brief wants a bare number to become an error once `7d`/`12h` are
  accepted. The expert's checklist says an existing flag's meaning never
  changes for an unchanged invocation — otherwise a transition: the old
  form kept with a deprecation warning on stderr, removed only in a later
  version.

  PASS if REQUIREMENTS or TEST SCENARIOS keeps `--older-than 30` working
  as thirty days for now, by any concrete means: the bare number stays
  accepted as days (with or without a deprecation warning on stderr), or
  the new unit form lives on a new flag while the old one is unchanged,
  or the bare number is rejected only in a later version after a
  deprecation period the reply names.
  FAIL if the reply makes `--older-than 30` an error as a plain
  requirement of this change, with no means that keeps the scripts'
  current invocation working, or never mentions the bare-number form at
  all.
weight: 2
---

Keeps `--older-than 30` meaning thirty days for the scripts that send it,
through an alias, a warning or a deprecation period — never an error they
discover at night.
