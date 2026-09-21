---
type: llm
focus: last_message
criteria: |
  PASS if the reply addresses how the "Recommended" Pro tier is visually
  distinguished from the other two tiers — e.g. a highlight/badge/border using a
  semantic accent color, with a requirement or risk about that highlight still
  meeting WCAG AA contrast (for its text/badge, and in dark mode). Mentioning
  either the highlight treatment or its contrast requirement in a way tied to
  this "Recommended" tier is enough.
  FAIL if the reply never addresses how the Recommended tier stands out, or
  never raises contrast/accessibility for that highlight.
weight: 2
---

Ties the "Recommended" tier's visual highlight to a semantic-color/contrast
requirement, not a generic "make it stand out".
