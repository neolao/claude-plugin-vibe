---
type: llm
focus: last_message
criteria: |
  fixtures/packages/api/ has no package-lock.json of its own. It is a
  member of the npm workspace declared by fixtures/package.json, whose
  fixtures/package-lock.json at the root resolves every member's
  dependencies: a workspace member never has its own lockfile.

  PASS if no `high` or `medium` severity `Version hygiene` finding says
  that fixtures/packages/api/ (or its package.json) lacks a lockfile or
  that its dependencies are unpinned because of it. Only a finding block
  (`PACKAGE:` ... `CATEGORY:` ... `SEVERITY:`) counts. A `Vulnerability`
  finding that says the audit could not run, whatever reason it gives, is
  not a Version hygiene finding and passes.
  FAIL if a `Version hygiene` finding at high or medium severity asks the
  member package for a lockfile of its own.
weight: 1
---

Does not ask a workspace member for a lockfile the root already commits.
