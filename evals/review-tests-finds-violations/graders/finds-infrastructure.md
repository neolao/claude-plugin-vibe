---
type: llm
focus: last_message
criteria: |
  PASS if the response reports that `TestUserServiceInfrastructure` in
  fixtures/test_user_service.py cannot run in this environment because it
  needs a real Postgres database (`psycopg2.connect(...)` — the driver, the
  server, or both are unavailable), and treats that inability as a finding
  in the `Infrastructure` category (or a clearly equivalent name) rather
  than passing over it in silence. It counts whether the agent learned this
  from the suite run or from reading the code.
  FAIL if the response never mentions that this test class could not run for
  lack of a database, or drops it without comment.
weight: 2
---

Reports the un-runnable Postgres-dependent test class as an `Infrastructure`
finding instead of silently skipping it.
