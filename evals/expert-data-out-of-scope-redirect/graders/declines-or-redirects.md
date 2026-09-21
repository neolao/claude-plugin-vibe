---
type: llm
focus: last_message
criteria: |
  The brief (which HTTP status code an endpoint should return, and how a
  repeated call should be answered) is a pure REST/HTTP-contract concern,
  entirely outside expert-data's domain (its own description names this
  exact case: "The API contract exposing the data → `expert-api-rest`").
  PASS if the sub-agent's reply is a brief, one-line style statement that it
  has no real concern in its domain here, optionally redirecting to
  expert-api-rest — and does NOT produce detailed, confident REQUIREMENTS/
  RISKS/TEST SCENARIOS picking status codes as if that were its own domain.
  FAIL if the reply fabricates specific HTTP-status-code advice (e.g. rules
  on 200 vs 204, or 409 vs 200) dressed up as data/persistence requirements.
weight: 2
---

Declines or redirects instead of inventing confident HTTP-status-code advice
outside its domain.
