---
type: llm
focus: last_message
criteria: |
  The brief renames `vault rm` to `vault delete`, and three teams' pipelines
  call `vault rm <name>`. The expert's checklist says subcommands are added,
  never renamed or removed, unless through a transition: the old form kept
  as an alias, with a deprecation warning on stderr, removed only in a later
  version.

  PASS if REQUIREMENTS keeps `vault rm` working as a name for the delete in
  this change (an alias, or the old subcommand left in place) and either
  warns about the deprecation on stderr or defers its removal to a later
  version.
  FAIL if the reply removes `vault rm` or makes it an error as part of this
  change, or never says what happens to the `vault rm` name.
weight: 2
---

Keeps `vault rm` alive through a transition instead of renaming it out from
under the pipelines that call it.
