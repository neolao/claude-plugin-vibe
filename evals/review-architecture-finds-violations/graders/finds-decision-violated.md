---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Decision violated` (or clearly
  equivalent category name) finding citing
  `.vibe/decisions/002-no-raw-sql-in-core.md` (or clearly describing its
  content) against `fixtures/core/order_service.py`'s direct `psycopg2`
  connection and raw SQL `INSERT`, which the decision explicitly forbids.
  FAIL if no finding references this decision as violated.
weight: 1
---

Reports core's raw SQL as violating decision 002 (core never talks to the
database directly), ideally with a `DECISION:` reference.
