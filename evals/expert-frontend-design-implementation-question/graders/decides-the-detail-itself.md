---
type: llm
focus: last_message
criteria: |
  Stacking versus horizontal scrolling at a phone width is a design detail
  the visual design expert picks itself; the invoking skill asked for a
  decision, not for a question to relay.

  PASS if the reply makes the call itself and nowhere hands it back: no
  "ask the Product Owner", no "this is a product decision", no
  `OPEN QUESTIONS:` list, no condition such as "if the business prefers X
  then …" that leaves the choice with someone else.
  FAIL if the reply defers the choice to the user, the Product Owner, the
  caller or "the team", frames it as a product decision, or lists it as an
  open question.
weight: 2
---

Decides the design detail itself instead of bouncing it to the Product Owner.
