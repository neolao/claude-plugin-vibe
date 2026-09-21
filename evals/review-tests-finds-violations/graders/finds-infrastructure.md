---
type: llm
focus: last_message
criteria: |
  PASS if the response's `SUITE EXECUTED`/`E2E/INTEGRATION EXECUTED` header
  or its findings note that `TestUserServiceInfrastructure` in
  fixtures/test_user_service.py could not run/complete because it depends
  on a real Postgres database (`psycopg2.connect(...)`) that is not
  available in this environment, reported as a finding rather than silently
  skipped, in the `Infrastructure` category (or clearly equivalent).
  FAIL if the response never mentions that this test/module could not run
  for lack of a database, or silently drops it without comment.
weight: 2
---

Reports the psycopg2/Postgres-dependent test as unable to run in this
environment, an `Infrastructure` finding, rather than silently ignoring it.
