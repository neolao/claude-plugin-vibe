---
type: llm
focus: last_message
criteria: |
  The app runs as six pods rolled out one at a time, so for the length of
  the rollout pods on the previous version still read and write
  `users.phone`, and the nightly CRM sync owned by another team reads it
  too. Renaming the column in the migration that ships with the new code
  makes every old pod fail on its next query. The expert's checklist says
  a column is never renamed or dropped while a version that still uses it
  runs, and that a rename is an expand/contract sequence.

  PASS if REQUIREMENTS or TEST SCENARIOS keeps `phone` in place while the
  old version runs, by a concrete sequence: a new `phone_number` column is
  added next to it, both are written (or the new one is backfilled from
  the old) until every reader has moved, and `phone` is dropped only in a
  later release — or the reply names the old pods and the CRM sync as what
  an in-place rename would break and requires that they keep working
  through the rollout.
  FAIL if the reply renames `phone` to `phone_number` in one migration as a
  plain requirement of this change, with no means that keeps the previous
  version's reads and writes working during the rollout, or never
  mentions the code still running on the old column.
weight: 2
---

Treats the rename as a change the running code would feel, and keeps the
old column readable and writable until every version and the CRM sync have
moved — never a rename the old pods discover mid-rollout.
