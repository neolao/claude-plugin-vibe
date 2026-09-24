---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Ubiquitous language` (or clearly
  equivalent category name) finding on fixtures/shop/dispatch.py for calling
  the shipment a `parcel` (`dispatch_parcel`, `parcel_id`,
  `pending_parcels`, the `parcel` locals) while the object it handles is
  the `Shipment` that `shipment.py`, `ShipmentRepository`, `reminders.py`
  and the `shipments` table all call a shipment. One concept, two names.
  FAIL if no finding flags the `parcel` / `shipment` split.
weight: 1
---

Reports the dispatch module renaming the shipment a `parcel` as a
Ubiquitous language finding.
