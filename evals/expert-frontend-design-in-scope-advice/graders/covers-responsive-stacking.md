---
type: llm
focus: last_message
criteria: |
  PASS if the reply specifies what happens to the three-column tier comparison
  table at narrow/phone widths — e.g. stacking the tiers vertically, making it
  swipeable/scrollable, or another concrete named layout — rather than leaving
  "responsive" unspecified. A TEST SCENARIOS entry exercising narrow-width
  behavior on this table also counts.
  FAIL if the reply never addresses the narrow-width behavior of the comparison
  table, or only says "make it responsive" with no concrete resolution.
weight: 2
---

Specifies a concrete narrow-width behavior for the three-tier comparison table
(stack/scroll/etc.), not just "make it responsive".
