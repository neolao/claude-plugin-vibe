---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS or TEST SCENARIOS defines the invoice line in at
  least one concrete respect: the unit price stored as an exact amount
  (`numeric`/`decimal` or integer minor units, never a float), the line
  kept immutable once the invoice is issued (no update path, or the
  invoice's issued state checked before any write), or a line that still
  reads correctly after its product is renamed, repriced or removed.
  FAIL if the line's shape is never defined beyond "copy the name and
  price", or if the unit price is stored as a float.
weight: 1
---

Defines the invoice line — the exact amount type, its immutability once
issued, or its independence from later product changes — instead of
spending the lists on a sync that must not exist.
