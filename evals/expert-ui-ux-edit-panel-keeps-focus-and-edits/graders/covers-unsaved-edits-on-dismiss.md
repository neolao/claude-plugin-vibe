---
type: llm
focus: last_message
criteria: |
  A panel over a table of a few hundred rows is dismissed in more ways than
  Save: Escape, a click on the table behind it, the Edit button of another
  row. Fields typed into and not saved are at stake each time.

  PASS if REQUIREMENTS, RISKS, or TEST SCENARIOS states, for this panel,
  what happens to typed-but-unsaved edits when it is dismissed without
  saving (Escape, clicking outside, opening another row's panel): they are
  kept, or an explicit confirmation precedes discarding them — not silently
  lost — with at least one of those dismissal paths named.
  FAIL if the reply never addresses unsaved edits on dismissal, or only
  covers the Save path and a plain Cancel click.
weight: 2
---

States what happens to unsaved edits when the panel is dismissed by Escape,
a click outside or another row's Edit — kept or confirmed, never silently
lost.
