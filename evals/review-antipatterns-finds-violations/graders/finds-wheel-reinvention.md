---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Wheel reinvention` (or clearly
  equivalent category name) finding on `parse_iso_date` in
  fixtures/date_utils.py, for hand-rolling an ISO-8601 date parser instead
  of using `datetime.fromisoformat` (or `dateutil`).
  FAIL if no finding flags `parse_iso_date` for this reason.
weight: 1
---

Reports the hand-rolled `parse_iso_date` as a Wheel reinvention finding.
