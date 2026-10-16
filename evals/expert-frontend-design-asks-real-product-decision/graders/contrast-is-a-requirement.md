---
type: llm
focus: last_message
criteria: |
  A customer can pick any brand color, including one on which white or dark
  text is unreadable. The expert's own checklist requires WCAG AA contrast,
  so this is settled: it is a requirement (or a risk with a stated
  resolution), not a question.

  PASS if the reply, in REQUIREMENTS or RISKS, requires that text and
  controls rendered on or in the customer's brand color stay readable —
  for example by deriving an accessible variant, choosing the foreground per
  color, or constraining the picker — in light and dark theme or at least
  without exception for the customer's choice.
  FAIL if contrast against an arbitrary customer color is never addressed,
  or is left to the Product Owner as an open question.
weight: 1
---

Treats the contrast of an arbitrary brand color as settled by its own
checklist — a requirement, not a question.
