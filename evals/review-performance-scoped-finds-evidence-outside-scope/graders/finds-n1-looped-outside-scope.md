---
type: llm
focus: last_message
criteria: |
  `describe` in fixtures/shipping/presenters.py awaits one `repo.carrier`
  query (fixtures/shipping/repo.py) per call; `list_shipments` in
  fixtures/api/app.py, outside the scope, calls it once per shipment of the
  customer, so a customer's list costs one carrier query per row where one
  batched query (or the `shipments_with_carrier_for_customer` join already
  in repo.py) would do.

  PASS if the reported findings include an `N+1` (or clearly equivalent
  category name) finding whose FILE: line points to
  fixtures/shipping/presenters.py or fixtures/shipping/repo.py, that names
  the per-shipment carrier query, and whose ISSUE or SUGGESTION names
  `list_shipments` or fixtures/api/app.py as the loop that repeats it.
  FAIL if no finding reports this per-shipment carrier query, or if the
  finding is anchored (its FILE: line) on fixtures/api/app.py.
weight: 2
---

Reports the per-call carrier query declared in scope, with the outside
loop as evidence: presenters.py alone shows a single query; only app.py,
outside the scope, shows it runs once per row.
