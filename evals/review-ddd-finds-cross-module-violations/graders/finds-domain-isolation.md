---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Domain isolation` (or clearly
  equivalent category name) finding on `Shipment` in
  fixtures/shop/shipment.py for importing `requests` and calling the
  carrier's HTTP API from `estimate_delivery`, i.e. a domain entity
  performing HTTP I/O itself.
  FAIL if no finding flags the HTTP call inside the `Shipment` entity, or if
  the only finding on it defers the whole issue to another agent without
  reporting it.
weight: 1
---

Reports the `Shipment` domain entity calling the carrier over HTTP as a
Domain isolation finding.
