---
type: llm
focus: last_message
criteria: |
  The expert's scope sentence keeps what the user does and what the
  interface tells them, and hands how it is rendered to
  `expert-frontend-design`: the focus ring's styling, and how a priority is
  rendered (weight, size, color), are that expert's checklist. Naming the
  priority is in scope (Save is the primary action, Delete is demoted);
  saying how to render it is not.

  PASS if no REQUIREMENTS, RISKS, or TEST SCENARIOS entry prescribes the
  panel's or its controls' appearance: a width or breakpoint, a color,
  shadow or overlay opacity, a type size, spacing, an animation or
  transition, the focus ring's color, thickness or style, or a button's
  visual weight or variant. "Focus is visible", "Save is the primary action
  and Delete is visually demoted", and "the row shows the new values" are
  statements of what the interface does or which action is primary, and
  pass.
  FAIL if any entry states such a visual property as a requirement, a risk
  or an expected result.
weight: 2
---

Prescribes nothing about how the panel, its buttons or the focus ring look —
that side of the boundary belongs to `expert-frontend-design`.
