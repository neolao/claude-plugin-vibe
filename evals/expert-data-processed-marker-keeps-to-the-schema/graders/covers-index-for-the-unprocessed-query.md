---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS, RISKS or TEST SCENARIOS names, tailored to this
  brief, that the job's query for rows not yet marked (`processed_at IS
  NULL` on a twenty-million-row `events` table that grows every day)
  needs a supporting index — a partial index on the unmarked rows, or an
  index on `processed_at` (with the ordering column) that the query uses —
  so each nightly run does not scan the whole table.
  FAIL if indexing of the unmarked-rows query is missing entirely, or only
  a generic "add an index" remark not tied to the `processed_at` query on
  the growing `events` table.
weight: 2
---

Names the index the job's unmarked-rows query needs on the growing
`events` table, tied to the brief's twenty million rows.
