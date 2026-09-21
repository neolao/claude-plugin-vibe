---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Trust boundary` (or clearly
  equivalent category name) finding on `charge_for_order`, which charges
  `order["total_cents"]` exactly as it appears in a file the partner uploads —
  the amount is never recomputed from the catalogue, bounded, or validated
  before the card is charged.
  FAIL if the unvalidated amount crossing into the payment call is not
  flagged.
weight: 1
---

Reports the partner-supplied charge amount as a Trust boundary finding.
