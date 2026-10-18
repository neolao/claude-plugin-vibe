---
type: llm
focus: trace
criteria: |
  Find the content of the written report in the trace: either a `cat` /
  `Read` of the `.vibe/reports/…-feature.md` file, or the `show` output of
  the counters right before `write`. If neither is in the trace, judge from
  the `report.sh` calls alone whether the resulting file would hold these
  values.
  PASS if the report (frontmatter between two `---` lines) carries
  `entry: feature`, `backlog: no`, `questions: 2`, `rounds: 1`,
  `findings.raised: 5`, `findings.dropped: 1`, `findings.merged: 2`,
  `findings.high: 1`, `findings.low: 1`, `returns.implementation: 1`,
  `fixes: 1`, and a `bricks:` block listing clarify, review and
  review-classifier with 1 each — and nothing else than statistics: no
  file path of the project, no finding text, no prose.
  FAIL if a value is wrong, if a key is missing, or if the report carries
  free text or project detail.
weight: 2
---

The report holds the right numbers and only numbers.
