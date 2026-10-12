---
type: llm
focus: trace
criteria: |
  Item 001 has `status: in_progress`. Items 002 and 004 list 001 in their
  `depends_on`; 003 does not.

  PASS if, before any file was removed or edited, the assistant asked for
  confirmation and that question (a) shows the item's number, title and
  status, (b) warns that the item is in progress, and (c) names 002 and 004
  as the items that depend on it and does not name 003 as one. The wording
  can differ from the skill's own.
  The trace is a raw event stream: an assistant message can show up in
  several events, and the skill's own instructions are also in it. Judge
  order by the assistant's own text events versus its `git rm`, `Write` and
  `Edit` tool calls: the question must be an assistant text event that comes
  before the first of them. A final report that only quotes the question
  afterwards does not count, and neither do the skill's instructions.
  FAIL if anything was removed or edited without asking first, or if the
  question lacks the in-progress warning or misses a dependent.
weight: 2
---

Step 3's confirmation fires first, with the in-progress warning and the right dependents.
