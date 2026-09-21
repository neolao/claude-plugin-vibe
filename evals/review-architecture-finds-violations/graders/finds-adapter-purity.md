---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Adapter purity` (or clearly
  equivalent category name) finding on `fixtures/adapters/postgres_gateway.py`,
  for either: `PostgresGateway.save` re-applying the promo discount itself
  (a business rule computed inside the adapter instead of trusted from
  core), or `PostgresGateway.notify` calling `EmailNotifier` directly
  instead of going back through core. Either one is enough to pass.
  FAIL if neither is flagged as an Adapter purity issue.
weight: 2
---

Reports either the business-rule duplication in `PostgresGateway.save` or
the adapter-to-adapter call in `PostgresGateway.notify` as an Adapter
purity finding.
