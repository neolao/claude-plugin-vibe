---
type: llm
focus: last_message
criteria: |
  The brief names the target: 60 fps on mid-range laptops. The expert's
  checklist makes it state the frame budget before design starts.

  PASS if the reply contains a numeric per-frame budget (16.6 ms, 16.7 ms or
  "about 16 ms", whether stated as given or as an assumption) AND at least
  one other millisecond or per-frame figure that bounds the labels or the
  picking pass.
  FAIL if no numeric budget appears, if the budget is only implied ("stay
  smooth"), if no cost of the plan is bounded by a figure, or if the frame
  rate or budget is put to the Product Owner as an open question.
weight: 1
---

States the numeric frame budget (16.6 ms at 60 fps) itself and bounds the
labels or the picking pass with a figure.
