---
type: llm
focus: last_message
criteria: |
  `/vibe:feature` relays every `OPEN QUESTIONS:` entry straight to a
  non-technical Product Owner, so a design detail the expert can pick itself
  must appear as a requirement, never as a question.

  PASS if no `OPEN QUESTIONS:` entry asks the Product Owner to settle a
  design detail of this kind: accepted logo formats, dimensions or aspect
  ratio; how text stays readable on a brand color with poor contrast; how
  the brand color behaves in dark mode; what the navigation bar does at
  narrow widths; which tokens or components carry the color. Having no
  `OPEN QUESTIONS:` list at all also passes this grader.
  FAIL if any `OPEN QUESTIONS:` entry asks one of those, or any other
  question the visual design expert could answer without the business.
weight: 2
---

Keeps pickable design details (logo constraints, contrast handling, dark
mode, narrow-width header) out of `OPEN QUESTIONS:`.
