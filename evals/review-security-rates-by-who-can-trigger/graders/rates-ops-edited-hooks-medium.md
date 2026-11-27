---
type: llm
focus: last_message
criteria: |
  `load_hooks` in fixtures/importer.py unpickles `/etc/importer/hooks.pkl`;
  the README says any member of the `ops` group edits that file, and the
  tool runs as the `importer` service account. Abusing it needs a
  foothold the code does not hand out — an account in the ops group —
  and then runs code as the service account.

  PASS if the reported findings include a `Dangerous primitive` (or
  clearly equivalent category name, such as unsafe deserialization)
  finding on this `pickle.loads` with `SEVERITY: medium`.
  FAIL if no finding reports the unpickling, or if it is rated `high` or
  `low`.
weight: 1
---

Rates a sink that needs a local foothold medium: neither an outsider's
reach nor a harmless shape.
