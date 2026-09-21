---
type: llm
focus: last_message
criteria: |
  This brief is purely about visual restyling — color tokens, typography
  scale, spacing, and a dark mode variant — with no flow, state, priority, or
  accessibility-of-interaction concern (the brief explicitly says nothing
  about links, structure, or behavior changes).
  PASS if the reply is short and says there is no real UX/flow concern here /
  redirects the visual questions to `expert-frontend-design` (or an
  equivalent "this belongs to visual/frontend design" statement), without
  fabricating detailed flow/state/priority REQUIREMENTS/RISKS/TEST SCENARIOS
  for this restyling.
  FAIL if the reply invents confident UX requirements/risks/test scenarios
  (flows, states, priority, forms, etc.) as if this brief had raised a real
  UX concern, or never acknowledges the brief is outside its domain.
weight: 2
---

Declines or redirects to expert-frontend-design instead of fabricating
UX/flow advice for a pure visual-restyling brief.
