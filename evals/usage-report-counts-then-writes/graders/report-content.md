---
type: llm
focus: trace
criteria: |
  Find the content of the written report in the trace: the result of the
  `cat` (or `Read`) of the `.vibe/usage-reports/…-feature.md` file made after
  `write`. FAIL if the trace holds no such content.
  PASS if the report (frontmatter between two `---` lines) carries
  `entry: feature`, `backlog: no`, `questions: 2`, `rounds: 1`,
  `findings.raised: 5`, `findings.dropped: 1`, `findings.merged: 2`,
  `findings.high: 1`, `findings.low: 1`, `returns.implementation: 1`,
  `fixes: 1`, and a `bricks:` block listing clarify, review and
  findings-classifier with 1 each — and nothing else than statistics: no
  file path of the project, no finding text, no prose.
  FAIL if a value is wrong, if a key is missing, or if the report carries
  free text or project detail.
weight: 2
---

The report holds the right numbers and only numbers.
