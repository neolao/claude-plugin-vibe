---
type: llm
focus: last_message
criteria: |
  PASS if the sub-agent's reply is a brief statement (roughly one line, or
  a short reply that explicitly says REST API contract design / backend
  request-response schemas are not its domain) that it has no real
  real-time-rendering concern here, and it does NOT invent detailed,
  confident REQUIREMENTS/RISKS/TEST SCENARIOS about endpoint shapes,
  pagination, status codes, or error body schemas as if that were its
  domain.
  FAIL if the reply designs or asserts confident detailed advice about the
  REST API contract, pagination, or error schema as if it were in scope.
weight: 2
---

Declines or redirects the REST API contract brief instead of fabricating
detailed domain advice for it.
