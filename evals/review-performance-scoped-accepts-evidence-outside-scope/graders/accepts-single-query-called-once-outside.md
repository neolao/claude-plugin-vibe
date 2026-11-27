---
type: llm
focus: last_message
criteria: |
  `describe` in fixtures/shipping/presenters.py awaits one `repo.carrier`
  query per call. Its only caller, `shipment_detail` in
  fixtures/api/app.py (outside the scope), calls it once per request for
  one shipment; `list_shipments` fetches a customer's shipments with the
  `shipments_with_carrier_for_customer` join of fixtures/shipping/repo.py
  and shapes the rows with `describe_row`, which runs no query.

  PASS if no `high` or `medium` severity `N+1` (or clearly equivalent
  category name) finding targets `describe`, `repo.carrier` or
  `list_shipments`. A `low` finding passes, and so does a report with no
  findings at all.
  FAIL if the per-call carrier query is reported as an N+1 at high or
  medium severity.
weight: 2
---

Does not call a single query an N+1 when its only caller, outside the
scope, calls it once per request and the list handler uses the join.
