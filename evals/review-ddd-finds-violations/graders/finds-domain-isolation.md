---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Domain isolation` (or clearly
  equivalent category name) finding on `close_order_route` in
  fixtures/order_routes.py, for embedding the $500 manager-approval business
  rule directly in the route handler and driving that domain decision off an
  HTTP status code (403) instead of the rule living in a domain/application
  layer.
  FAIL if no finding flags this rule's placement in the route handler.
weight: 2
---

Reports the approval business rule embedded in the Flask route handler as a
Domain isolation finding.
