---
type: llm
focus: last_message
criteria: |
  PASS if the reply (in REQUIREMENTS, RISKS, or TEST SCENARIOS) calls for reusing
  the existing design system — tokens, type scale, spacing scale, and/or component
  library — for the new pricing page, and for the "Recommended" tier and dark mode
  to work through that same system rather than one-off/ad-hoc styling. It is fine
  if it is phrased around the pricing page specifically (e.g. "the pricing table
  and tier cards must use existing tokens/components, including in dark mode").
  FAIL if the reply never mentions reusing the design system/tokens/dark mode, or
  only gives a generic "be consistent" statement with no tie to this page.
weight: 2
---

Names token/component/dark-mode reuse as a requirement or risk for this specific
pricing page, not a generic restatement of "keep it consistent".
