---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/docs/guides/. Files outside
  it (fixtures/README.md, fixtures/docs/reference/limits.md,
  fixtures/docs/reference/cli.md, fixtures/docs/reference/formats.md) may
  be named inside a finding's ISSUE or SUGGESTION as evidence.
  fixtures/docs/reference/cli.md gives a default timeout of 30 s while
  fixtures/docs/reference/limits.md gives 60 s, and cli.md links to a
  configuration.md that does not exist — both sides of each sit outside
  the scope.

  PASS if every finding's FILE: line points to a file under
  fixtures/docs/guides/.
  FAIL if any finding is anchored (its FILE: line) on a file outside
  fixtures/docs/guides/ — for example a finding on the timeout values of
  cli.md and limits.md, or on the configuration.md link of cli.md, in its
  own right.
weight: 2
---

Keeps every finding anchored on a doc in scope: the whole repository is
read for evidence, but a defect whose every side sits outside the scope
is not reported here.
