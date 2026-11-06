---
type: llm
focus: last_message
criteria: |
  In the fixture, `core/invoice_service.py` and `core/export_service.py`
  both `from adapters.s3_storage import upload`, while
  `.vibe/modules/core.md` gives `core` no dependency and
  `.vibe/decisions/001-dependencies-point-inward.md` decides that `core/`
  never imports `adapters/`. The expert's rule: an idiom in the repo wins,
  but an import against the direction the repo's own layering enforces, or
  a recorded decision contradicted, stays a defect whatever the neighbours
  do.

  PASS if the reply says that the existing `core` → `adapters.s3_storage`
  import reverses the dependency direction the module map or the decision
  enforces (any wording: wrong direction, violates decision 001, core
  depending on an adapter, inward rule broken), as a risk, a weak criterion
  of the copy-the-neighbours option, or a reason it loses.
  FAIL if the reply presents the direct import as the repo's idiom to follow
  without naming the reversed direction, or never mentions that the two
  existing services contradict the map or the decision.
weight: 2
---

Names the neighbours' core-to-adapter import as a reversed dependency that
the module map and the decision forbid, instead of calling it the idiom.
