---
type: llm
focus: last_message
criteria: |
  Only a finding block (a `FILE:` line with its CATEGORY, SEVERITY, ISSUE
  and SUGGESTION) counts; a sentence outside any finding block does not.
  PASS if no finding is anchored on `Slot` in fixtures/studio/slot.py or on
  `AttendanceLine` in fixtures/reports/attendance.py for being compared or
  hashed by value, lacking an id, or needing an identity. A report whose
  only findings are elsewhere passes.
  FAIL if any finding asks `Slot` or `AttendanceLine` to gain an identity or
  to stop comparing by value.
weight: 1
---

Leaves the frozen value object and the read model alone: both compare by value
on purpose.
