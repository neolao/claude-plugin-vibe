---
type: llm
focus: last_message
criteria: |
  The request forbids a new dependency. `tenacity` is imported in
  fixtures/notify.py and added to fixtures/requirements.txt.

  PASS if a `(constraint)` finding quotes the no-new-dependency constraint
  and points at `tenacity` (the import and/or the requirements line), with a
  fix (drop it).
  FAIL if the new dependency is not reported as a breached constraint.
weight: 2
---

A breach hidden in a manifest, not in the code logic, is still a breach.
