---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/archiver/lib/.
  fixtures/archiver/store.py, outside the scope, holds `save_share`, which
  builds its INSERT with an f-string from `doc_id`, the CLI argument of
  `archiver share`: the query, the argument and every call between them
  sit outside the scope, and no file under fixtures/archiver/lib/ takes
  part in it.

  PASS if no finding reports `save_share` or its f-string INSERT —
  whatever its severity and wherever its FILE: line points. A report with
  no findings at all passes, and so does a sentence outside any finding
  block saying the concatenated query exists but is out of scope.
  FAIL if any finding (a FILE: block) reports `save_share` or its INSERT.
weight: 2
---

Reports nothing on a SQL concatenation whose query and argument both sit
outside the scope, however clear: the full review owns it.
