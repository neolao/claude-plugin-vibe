---
type: llm
focus: last_message
criteria: |
  PASS if the sub-agent's reply is a brief statement (roughly one line, or
  a short REQUIREMENTS/RISKS/TEST SCENARIOS reply that explicitly says
  threat modeling / access-control / RBAC design is not its domain and
  redirects it elsewhere) that it has no real operational concern here, and
  it does NOT invent detailed, confident REQUIREMENTS/RISKS/TEST SCENARIOS
  about the authorization model, role scheme, or threat model itself.
  A reply is also acceptable if it notes a genuinely operational adjacent
  concern (e.g. audit logging of access events) while still declining to
  design the threat model / RBAC scheme.
  FAIL if the reply designs or asserts confident detailed advice about the
  threat model, roles/permissions, or privilege-escalation detection as if
  it were in scope.
weight: 2
---

Declines or redirects the threat-modeling/access-control brief instead of
fabricating detailed domain advice for it.
