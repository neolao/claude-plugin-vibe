---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `N+1` (or clearly equivalent
  category name) finding for the carrier query issued once per shipment when
  `list_shipments` in fixtures/shipping/app.py builds its response: each
  `presenters.describe` call awaits `repo.carrier(db, ...)`, one query per
  row of the customer's shipments, instead of fetching the needed carriers in
  one batched query. The finding may be anchored in app.py, presenters.py or
  repo.py, as long as it names this per-shipment carrier query.
  FAIL if no finding flags this per-shipment carrier query.
weight: 2
---

Reports the per-shipment `repo.carrier` query reached from `list_shipments`
as an `N+1`. The loop is in app.py, the query is issued from presenters.py:
neither file shows the pattern on its own.
