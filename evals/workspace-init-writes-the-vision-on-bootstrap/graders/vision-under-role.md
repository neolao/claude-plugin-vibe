---
type: llm
focus:
  source: file
  path: roadmap/CLAUDE.md
criteria: |
  Read the `## Role` section of this hub CLAUDE.md (from the `## Role`
  heading to the next `## ` heading).

  PASS if, inside that section, there is a paragraph describing what
  this workspace is for — a florist taking orders online and delivering
  them the same day, with the API owning the orders and the storefront
  selling them (a rewording that keeps that substance is fine) — in
  addition to the fixed sentences about cross-repo planning and
  non-implementable items.
  FAIL if no such paragraph is in the `## Role` section (missing
  altogether, or placed in another section or file), or if it is only a
  placeholder.
weight: 2
---

The vision lands under `## Role`, where a later refresh will look for it
to carry it over.
