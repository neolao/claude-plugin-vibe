---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS, RISKS or TEST SCENARIOS addresses what the new
  column means for the twenty million rows that exist when it is added:
  they are all unmarked, so the first run would export them again unless
  the rows already sent are marked before the job first runs (a batched
  backfill up to a cutoff) or the job's query is bounded to events after
  the switch — any concrete means that keeps the first run from re-sending
  two years of events passes.
  FAIL if the reply never mentions the existing rows and what the first
  run does with them, or marks them all in one update of the whole table.
weight: 2
---

Settles what the first run does with the twenty million existing rows —
marked in batches before the switch, or excluded by a cutoff — instead of
leaving them to be exported again.
