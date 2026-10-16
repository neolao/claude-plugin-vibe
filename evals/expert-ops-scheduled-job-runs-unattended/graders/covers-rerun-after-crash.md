---
type: llm
focus: last_message
criteria: |
  The job pushes many orders per run and stores the partner's shipment id on
  each order after the call. A run can die halfway through a backlog (the pod
  is evicted, the partner times out, the image is rolled): the next run must
  not push again the orders that already have a shipment, and the window
  between the partner call succeeding and the id being stored is where a
  rerun creates a second shipment.

  PASS if REQUIREMENTS, RISKS, or TEST SCENARIOS names, for this job, that a
  rerun after a crash mid-way must not create a second shipment for an order
  already pushed, and says how: selecting only orders without a shipment id
  and recording the id per order before moving on, an idempotency key or
  client reference per order on the partner call, a claimed/in-progress
  state, or an equivalent — not only "retries with backoff".
  FAIL if the reply never raises what happens to orders already pushed when
  a run dies and the next one starts, or covers it only as a generic retry
  statement with no tie to the stored shipment id or to duplicate shipments.
weight: 2
---

Requires a rerun after a crash mid-backlog to create no second shipment for
an order already pushed, anchored on the shipment id the job stores.
