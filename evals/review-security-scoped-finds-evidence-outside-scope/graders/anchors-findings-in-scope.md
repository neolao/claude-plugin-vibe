---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/archiver/lib/. Files outside it
  (fixtures/archiver/cli.py, commands.py, manifest.py, tokens.py, store.py,
  accounts.py) may be named inside a finding's ISSUE or SUGGESTION as the
  entry point that feeds a helper or the place to fix. fixtures/archiver/
  store.py holds `save_share`, which builds its INSERT with an f-string
  from `doc_id`, the CLI argument of `archiver share`: the query, the
  argument and every call between them sit outside the scope, and no file
  under fixtures/archiver/lib/ takes part in it.

  PASS if every finding's FILE: line points to a file under
  fixtures/archiver/lib/, and no finding reports `save_share` or its
  f-string INSERT — whatever its FILE: line. A sentence outside any finding
  block saying that `save_share` concatenates SQL but is out of scope
  passes.
  FAIL if any finding is anchored (its FILE: line) on a file outside
  fixtures/archiver/lib/, or if any finding (a FILE: block) reports
  `save_share` or its INSERT.
weight: 2
---

Keeps every finding anchored on a file in scope and leaves a defect whose
both ends sit outside the scope alone, however clear: the whole repository
is read for evidence, and the full review owns the rest.
