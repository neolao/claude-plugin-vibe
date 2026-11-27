---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/portal/routes/. Files outside
  it (fixtures/portal/app.py, storage.py, users.py, orders.py) may be named
  inside a finding's ISSUE or SUGGESTION as the helper a route calls, the
  hook that does or does not guard it, or the place to fix.
  fixtures/portal/app.py holds `export`, which passes the client's `rows`
  query parameter to `storage.render_export` with no upper bound: the
  route, the parameter and the loop all sit outside the scope, and no file
  under fixtures/portal/routes/ takes part in it.

  PASS if every finding's FILE: line points to a file under
  fixtures/portal/routes/, and no finding reports `export`, `render_export`
  or the uncapped `rows` — whatever its FILE: line. A sentence outside any
  finding block saying that `export` is uncapped but out of scope passes.
  FAIL if any finding is anchored (its FILE: line) on a file outside
  fixtures/portal/routes/, or if any finding (a FILE: block) reports
  `export`, `render_export` or `rows`.
weight: 2
---

Keeps every finding anchored on a file in scope and leaves a defect whose
both ends sit outside the scope alone, however clear: the whole repository
is read for evidence, and the full review owns the rest.
