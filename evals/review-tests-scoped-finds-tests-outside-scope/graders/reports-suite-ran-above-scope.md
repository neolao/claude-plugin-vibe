---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/src/billing/. The suite is
  configured in fixtures/package.json and lives in fixtures/tests/, both
  above that path; it runs green (`npm test` → 4 tests, all passing).

  PASS if the `SUITE EXECUTED:` line names the command that ran (`npm
  test` or `node --test ...`) and reports the run's result with counts
  (passed / failed / skipped, or an equivalent summary).
  FAIL if that line says the suite could not run, was NOT RUN, that no
  runner or no tests were found, or if the line is missing.
weight: 2
---

Runs the suite configured above the scope and reports its real result,
instead of declaring the scope untested or the runner missing.
