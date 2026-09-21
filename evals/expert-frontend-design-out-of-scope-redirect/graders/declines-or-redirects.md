---
type: llm
focus: last_message
criteria: |
  This brief is purely about checkout flow steps, state preservation across
  steps/sessions, and failure handling — no visual design concern (typography,
  spacing, color, responsive layout, visual consistency) is present.
  PASS if the reply is short and says there is no real visual-design concern
  here / redirects the flow-and-state questions to `expert-ui-ux` (or an
  equivalent "this belongs to UI/UX" statement), without fabricating detailed
  visual-design REQUIREMENTS/RISKS/TEST SCENARIOS for this checkout flow.
  A one-line "no concern in my domain, see expert-ui-ux for the flow/state
  questions" is exactly what should happen.
  FAIL if the reply invents confident visual-design requirements/risks/test
  scenarios (colors, spacing, typography, responsive behavior, etc.) as if this
  brief had raised a real visual-design concern, or never acknowledges the
  brief is outside its domain.
weight: 2
---

Declines or redirects to expert-ui-ux instead of fabricating visual-design
advice for a pure flow/state brief.
