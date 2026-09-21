---
type: llm
focus: trace
criteria: |
  PASS if, before creating any backlog file, the assistant asked whether to
  split the request into separate items, and that question names (or clearly
  paraphrases) the three candidate titles — something covering CSV export,
  something covering dark mode, and something covering email notifications —
  as distinct items. The exact wording can differ from the skill's own
  template ("This description seems to cover several distinct features: […].
  Do you want me to create a separate item for each?") as long as the intent
  and the three candidates are both clearly present.
  FAIL if backlog files were created without ever asking, if the question was
  asked but did not name distinct candidate titles, or if the question was
  asked only after files had already been written.
weight: 2
---

Confirms the oversized-scope confirmation question (Step 6) fired, naming
the three candidate titles, before any file was created.
