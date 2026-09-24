---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Repository` (or clearly
  equivalent category name) finding on `ShipmentRepository.find_overdue` in
  fixtures/shop/shipment_repository.py returning raw SQL rows (`fetchall()`)
  instead of `Shipment` objects like its sibling methods, or on
  `late_shipment_notices` in fixtures/shop/reminders.py reading those rows
  by column index (`row[0]`, `row[4]`, `row[6]`). Either anchor is enough.
  FAIL if no finding flags these raw rows.
weight: 1
---

Reports `find_overdue` leaking raw rows, read by index in the reminder job,
as a Repository finding.
