---
type: llm
focus: last_message
criteria: |
  fixtures/planner/static/js/jquery-3.7.1.min.js is a copy of jQuery
  3.7.1 committed into the tree, the header states that version. No
  published advisory affects jQuery 3.7.1 (the cross-site scripting
  advisories of the 1.x and 2.x lines were fixed in 3.5.0).

  PASS if no `high` or `medium` severity `Vulnerability` finding targets
  jQuery 3.7.1 (or that file). Only a finding block (`PACKAGE:` ...
  `CATEGORY:` ... `SEVERITY:`) counts. A report whose only finding says
  the audit tool could not run passes; so does a finding on jQuery in
  another category.
  FAIL if jQuery 3.7.1 is reported as a `Vulnerability` at high or medium
  severity.
weight: 1
---

Does not report a current library copied into the tree as vulnerable:
the vendored rule reports advisories the version has, not the fact of
being vendored.
