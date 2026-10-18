---
type: llm
focus: trace
criteria: |
  Read the `usage-report.sh` calls in the trace (Bash tool). Each event of the
  prompt must have been counted with the matching operation, at the moment
  it was listed, not all at once at the end:
  - `brick clarify`, `brick review`, `brick findings-classifier` (one each);
  - `incr questions 2` (or two `incr questions`);
  - `incr findings.raised 5`;
  - `incr findings.dropped 1`, `incr findings.merged 2`,
    `incr findings.high 1`, `incr findings.low 1`;
  - `incr returns.implementation` and `incr rounds` (one each);
  - `incr fixes` (one).
  Chaining several calls with `&&` in one Bash call is fine. Counting the
  same quantity through a different key (e.g. `findings.medium` for the
  high finding) is a FAIL. Counting everything in a single batch right
  before `write`, after narrating all the events, is a FAIL.
  PASS when every event above is counted with the right key and quantity
  and no counter was edited by hand (Write/Edit on `usage-report.tsv`).
weight: 3
---

Every event reaches the counters through the script with the right key, as
it happens.
