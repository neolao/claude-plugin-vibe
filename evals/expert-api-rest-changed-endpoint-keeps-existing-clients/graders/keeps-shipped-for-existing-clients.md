---
type: llm
focus: last_message
criteria: |
  Three partner integrations branch on the `status` value, one of them
  emailing its customer when it sees `shipped`, and the brief says partners
  update their code on their own schedule. Replacing `shipped` with
  `dispatched` and `delivered` in the response those partners already get
  silently breaks that workflow.

  PASS if REQUIREMENTS, RISKS or TEST SCENARIOS requires that a partner's
  unchanged request keeps getting a status it understands, by any one
  concrete means: `shipped` stays in the existing response and the finer
  state goes into a new field, the new values appear only on a new API
  version or a new endpoint while the old one keeps `shipped` until the
  partners have moved, or an explicit opt-in (a version header or
  parameter) before a client sees the new values.
  FAIL if the reply treats the split as a plain value change (rename
  `shipped`, document it, notify the partners) with no means that keeps the
  existing response unchanged for clients that have not moved, or only says
  "communicate the change" without such a means.
weight: 2
---

Requires that partners who branch on `shipped` keep receiving it on their
unchanged requests, through a new field, a version or an opt-in — never a
rename they discover in production.
