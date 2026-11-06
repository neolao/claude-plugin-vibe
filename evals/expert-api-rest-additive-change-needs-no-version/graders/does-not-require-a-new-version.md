---
type: llm
focus: last_message
criteria: |
  The brief adds one optional response field and one optional query filter
  and changes nothing that exists; the partners' clients ignore unknown
  fields by the API guide's rule. The expert's own checklist says an
  additive change needs no new version.

  PASS if no REQUIREMENTS entry demands a new API version (`/v2`, a version
  header), a new endpoint in place of the existing ones, or a deprecation
  cycle for this change. Stating that the change is additive and that the
  existing fields and order stay unchanged is expected and passes; a RISKS
  entry noting that a partner client might still break on an unknown field
  despite the guide, with a test for it, also passes.
  FAIL if REQUIREMENTS requires versioning the endpoints, duplicating them,
  or running a deprecation period as the condition for adding the optional
  field or the filter.
weight: 2
---

Does not reach for a new API version on an additive change: the
compatibility rule triggers on what existing clients would feel, and here
they feel nothing.
