---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/docs/guides/.
  fixtures/README.md, outside the scope, lists
  docs/reference/retention.md, which does not exist; no guide links to
  that page.

  PASS if no finding names retention.md (or the retention entry of the
  README) as a dangling reference, an index entry that does not exist or
  any other defect — whatever its severity and wherever its FILE: line
  points. A report with no findings at all passes, and so does a sentence
  outside any finding block saying the entry is broken but out of scope.
  FAIL if any finding (a FILE: block) reports the retention entry.
weight: 2
---

Reports nothing on a dangling index entry whose index and target both sit
outside the scope: neither side is a file the agent was given.
