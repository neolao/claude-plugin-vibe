---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/portal/routes/.
  fixtures/portal/app.py holds `export`, which passes the client's `rows`
  query parameter to `storage.render_export` with no upper bound: the
  route, the parameter and the loop all sit outside the scope, and no file
  under fixtures/portal/routes/ takes part in it. Files outside the scope
  may be named inside a finding's ISSUE or SUGGESTION as the helper a
  route calls or the hook that guards it.

  PASS if every finding's FILE: line, if any, points to a file under
  fixtures/portal/routes/, and no finding reports `export`,
  `render_export` or the uncapped `rows` — whatever its FILE: line. A
  report with no findings at all passes, and so does a sentence outside
  any finding block saying that `export` is uncapped but out of scope.
  FAIL if any finding is anchored (its FILE: line) on a file outside
  fixtures/portal/routes/, or if any finding (a FILE: block) reports
  `export`, `render_export` or `rows`.
weight: 2
---

Leaves a defect whose both ends sit outside the scope alone, however
clear, and anchors nothing outside the scope.
