---
type: llm
focus: last_message
criteria: |
  The recorded decision says `core/` owns the ports it needs and
  `adapters/` implements them; `app.py` wires them. The expert must
  recommend an option that holds that direction for the new statement
  code.

  PASS if the RECOMMENDATION (or the single option, if the reply gives only
  one) has the statement-building code in `core/` depend on an abstraction
  core owns (a storage port or protocol in `core/`, an injected `save` or
  storage object passed in by `app.py`) rather than importing
  `adapters.s3_storage` — the S3 upload itself stays in `adapters/`. Leaving
  the two existing services as they are, or listing their migration as a
  separate step, is fine.
  FAIL if the recommended option imports `adapters.s3_storage` (or any
  `adapters` module) from the new core code because the neighbours do, or
  moves the statement building into `adapters/` to reach S3.
weight: 2
---

Recommends an option in which the new core code reaches S3 through a port or
an injected dependency, not through the neighbours' direct adapter import.
