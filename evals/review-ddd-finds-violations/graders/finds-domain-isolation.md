---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Domain isolation` (or clearly
  equivalent category name) finding on `close_order_route` in
  fixtures/order_routes.py, for embedding the $500 manager-approval business
  rule directly in the route handler instead of the rule living in a
  domain/application layer. Mentioning that the decision is expressed as an
  HTTP status code (403) is welcome but not required.
  FAIL if no finding flags this rule's placement in the route handler.
weight: 2
---

Reports the approval business rule embedded in the Flask route handler as a
Domain isolation finding.
