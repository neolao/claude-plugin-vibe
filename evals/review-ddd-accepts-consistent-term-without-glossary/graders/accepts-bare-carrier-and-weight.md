---
type: llm
focus: last_message
criteria: |
  `Batch.carrier` in fixtures/logistics/batch.py is a bare string and
  `Parcel.weight_grams` a bare integer; no source names a Carrier or Weight
  concept, and no rule in the code applies to either.

  PASS if no `high` or `medium` severity Value object or Ubiquitous
  language finding asks for a `Carrier`, `Weight` or similar type around
  those fields. A report with no findings at all passes.
  FAIL if either field is flagged for that reason at high or medium
  severity.
weight: 1
---

Leaves a bare primitive alone: a primitive that could become a value
object is review-antipatterns' primitive obsession, never a finding here.
