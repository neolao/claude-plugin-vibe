---
type: llm
focus: last_message
criteria: |
  The brief names no target frame rate: the expert's checklist makes the
  frame budget a value it states itself before design starts (from the
  brief's target rate and hardware, else 16.6 ms at 60 fps), and the
  per-frame work above is sized against it.

  PASS if the reply states a numeric per-frame budget — 16.6 ms at 60 fps
  (16.7 ms or "about 16 ms" count), or another figure with a reason drawn
  from the brief's hardware — and uses it to bound at least one of the
  streaming costs (decode, upload, or shader compilation per frame).
  FAIL if no numeric budget appears, if the budget is only implied ("stay
  smooth", "no hitches"), or if the target frame rate or budget is put to
  the Product Owner as an open question instead of being stated.
weight: 1
---

States a numeric frame budget itself (16.6 ms at 60 fps when the brief names
no target) instead of asking for it or leaving it implied.
