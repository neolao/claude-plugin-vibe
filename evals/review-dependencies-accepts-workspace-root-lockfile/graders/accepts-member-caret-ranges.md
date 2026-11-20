---
type: llm
focus: last_message
criteria: |
  fixtures/packages/api/package.json declares `express: ^4.21.2` and
  `date-fns: ^3.6.0`. It is a member of the npm workspace declared by
  fixtures/package.json, and fixtures/package-lock.json at the root
  resolves both (express 4.21.2, date-fns 3.6.0): the caret ranges are
  backed by a committed lockfile, the ecosystem's convention.

  PASS if no `high` or `medium` severity `Version hygiene` finding targets
  `express` or `date-fns` for its caret range. Only a finding block
  (`PACKAGE:` ... `CATEGORY:` ... `SEVERITY:`) counts. A report whose only
  finding says the audit tool could not run passes.
  FAIL if either caret range is flagged as `Version hygiene` at high or
  medium severity.
weight: 1
---

Does not call a workspace member's caret ranges floating: the root
lockfile resolves them.
