---
date: 2026-01-10
status: accepted
---
# Missing readings are skipped, never an error

**Context:** Sensor lists contain `null` where a reading was lost; every statistics helper receives such lists.
**Decision:** A statistics helper ignores `null` entries and computes on the remaining numbers. A list with no number left is the empty-list case.
**Reason:** The dashboard must still show a value for a day with one lost reading; treating `null` as invalid input hid whole days.
**Rejected alternatives:** Cleaning the list in every caller (forgotten twice); treating `null` as zero (wrong values).
