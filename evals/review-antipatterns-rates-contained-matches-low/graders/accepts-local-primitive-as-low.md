---
type: llm
focus: last_message
criteria: |
  `shipping_fee` in fixtures/receipts/fees.py takes and returns `Money`;
  the bare integer `fee_cents` exists only inside the function body.

  PASS if no `high` or `medium` severity Primitive obsession (or
  equivalent) finding targets `fee_cents` or `shipping_fee`. A `low`
  finding passes, as does a report with no findings at all.
  FAIL if `fee_cents` / `shipping_fee` is flagged at high or medium
  severity for bare money.
weight: 1
---

A bare primitive that never leaves one function is a contained match:
`low` at most.
