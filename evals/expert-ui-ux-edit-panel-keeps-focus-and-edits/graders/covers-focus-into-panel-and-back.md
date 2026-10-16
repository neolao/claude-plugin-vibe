---
type: llm
focus: last_message
criteria: |
  The panel is built for this page, over a table that warehouse staff work
  from the keyboard many rows in a row. Where keyboard focus goes when the
  panel opens and when it closes decides whether that is possible: focus
  left behind the panel means tabbing through the table under it; focus
  dropped on close means starting again from the top of the page after
  every row.

  PASS if REQUIREMENTS or TEST SCENARIOS states, for this panel, both that
  opening it moves keyboard focus into it (its first field or its heading)
  and that closing it — by Save, by Cancel or Escape — returns focus to the
  Edit button or row that opened it (or an equivalent stated place in the
  table next to that row, so the user continues from where they were).
  FAIL if focus placement is never addressed, if only one of the two
  directions (into the panel, back to the row) is covered, or if the reply
  stays at "keyboard accessible" / "visible focus" / "proper focus
  management" without saying where focus goes on open and on close.
weight: 2
---

Requires focus to move into the panel when it opens and back to the row
that opened it when it closes, so a keyboard user continues from where they
were.
