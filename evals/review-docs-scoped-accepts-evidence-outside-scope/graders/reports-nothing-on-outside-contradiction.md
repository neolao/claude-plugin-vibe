---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/docs/guides/.
  fixtures/docs/reference/cli.md gives the reconciliation timeout a
  default of 30 s; fixtures/docs/reference/limits.md gives 60 s. Both
  files sit outside the scope and no guide mentions the timeout.

  PASS if no finding reports the timeout values, cli.md or limits.md's
  timeout row as a contradiction — whatever its severity and wherever its
  FILE: line points. A report with no findings at all passes, and so does
  a sentence outside any finding block saying the disagreement exists but
  is out of scope.
  FAIL if any finding (a FILE: block) reports the 30 s / 60 s
  disagreement.
weight: 2
---

Reports nothing on a contradiction whose two sides both sit outside the
scope, however visible: the scope bounds what is reported, not what is
read, and the full review owns it.
