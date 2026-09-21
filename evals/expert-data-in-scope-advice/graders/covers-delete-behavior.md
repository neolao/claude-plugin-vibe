---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS, RISKS, or TEST SCENARIOS names, tailored to this
  brief, that keeping cancelled-order rows instead of deleting them is a
  deliberate delete-behavior choice (e.g. a status/soft-delete flag rather
  than a physical delete) that must still be enforced consistently — for
  instance via a constraint, a documented status value, or an index/query
  update so cancelled orders aren't silently included/excluded where they
  shouldn't be.
  FAIL if this deliberate delete-behavior point is missing entirely, or only
  a generic "consider soft deletes" remark not tied to the brief's accounting
  retention need.
weight: 2
---

Names the deliberate delete-behavior/retention choice for cancelled orders
as a concrete requirement or risk, tied to the brief's accounting-retention
need.
