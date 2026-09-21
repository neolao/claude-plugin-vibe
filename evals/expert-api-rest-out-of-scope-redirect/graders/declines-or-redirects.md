---
type: llm
focus: last_message
criteria: |
  The brief (a new `orders` column type, nullability, and indexing decision)
  is a pure database-schema concern, entirely outside expert-api-rest's
  domain (its own description names this exact case: "Database schema →
  `expert-data`").
  PASS if the sub-agent's reply is a brief, one-line style statement that it
  has no real concern in its domain here, optionally redirecting to
  expert-data — and does NOT produce detailed, confident REQUIREMENTS/RISKS/
  TEST SCENARIOS about column types, nullability, or indexing as if that were
  its own domain.
  FAIL if the reply fabricates specific database-schema advice (e.g. picks a
  column type, rules on nullability, or prescribes an index) dressed up as
  REST-API requirements/risks.
weight: 2
---

Declines or redirects instead of inventing confident database-schema advice
outside its domain.
