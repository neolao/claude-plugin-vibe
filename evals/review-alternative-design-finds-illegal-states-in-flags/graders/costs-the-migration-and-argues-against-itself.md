---
type: llm
focus: last_message
criteria: |
  The agent's definition requires every published proposal to count its
  migration in files touched (grepped, not estimated) and to state the
  strongest argument against itself in one sentence.

  PASS if every finding that proposes an alternative design gives a
  migration cost as a number of files (for example "4 files:
  orders/order.py, orders/repository.py, api/handlers.py,
  api/warehouse_job.py") and contains a counter-argument against its own
  proposal (a sentence saying what the proposal costs or when it would be
  wrong, such as the reading cost of a pattern the repo does not use yet).
  Work that is not a file of the repository (a schema change, a data
  backfill) named next to the file count does not make the count fail.

  FAIL if any proposal lacks a number of files for its migration, or has no
  argument against itself.
weight: 1
---

Every proposal is costed in files and carries its own counter-argument: a
proposal without them is the noise the agent exists to avoid.
