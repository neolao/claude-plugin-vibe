---
type: llm
focus: last_message
criteria: |
  fixtures/api/routes.py serves `/buyers/<buyer_id>/orders` and emits
  `buyer_id` for the concept the domain calls a customer.
  `.vibe/decisions/001-buyer-kept-in-public-api.md` (status accepted)
  mandates exactly that: the API keeps `buyer` until the mobile app ships
  the rename.

  PASS if no `high` or `medium` severity Ubiquitous language (or
  equivalent) finding targets the `buyer` of fixtures/api/routes.py. A
  report with no findings at all passes, as does a report that names the
  decision as the reason for staying silent.
  FAIL if the `buyer` / `customer` split is flagged at high or medium
  severity.
weight: 2
---

Does not reopen a legacy name a recorded decision keeps.
