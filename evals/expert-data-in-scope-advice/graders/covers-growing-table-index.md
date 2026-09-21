---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS, RISKS, or TEST SCENARIOS names, tailored to this
  brief, that the dashboard's "list orders sorted by creation date, filtered
  by status" query needs a supporting index (e.g. a composite index on
  status + creation date) because the `orders` table already has 5 million
  rows and is growing — calling out the risk of an unbounded/unindexed scan
  on this specific table.
  FAIL if indexing is missing entirely, or only a generic "add indexes as
  needed" remark not tied to the 5-million-row orders table and its
  sort/filter query.
weight: 2
---

Names the index needed for the orders-by-date/status dashboard query as a
concrete requirement or risk, tied to the brief's 5-million-row growing
table.
