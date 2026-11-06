---
type: llm
focus: last_message
criteria: |
  No file imports fixtures/jobs/nightly.py, the only file of the `jobs`
  module. fixtures/pyproject.toml declares it as the `nightly` console
  script (`[project.scripts] nightly = "jobs.nightly:main"`), and the
  module's `Role:` says each run is its own process that builds its own
  gateway.

  PASS if no `high` or `medium` severity Orphaned module finding targets
  the `jobs` module or fixtures/jobs/nightly.py, and no `high` or `medium`
  severity Wiring finding targets its `PostgresGateway()` construction.
  A report with no findings at all passes.
  FAIL if `jobs` is reported as orphaned, or its construction as wiring
  drift, at high or medium severity.
weight: 1
---

Does not call a module a manifest loads by name an orphan.
