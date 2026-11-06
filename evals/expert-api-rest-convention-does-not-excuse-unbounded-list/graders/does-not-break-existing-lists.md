---
type: llm
focus: last_message
criteria: |
  Five apps written by other teams read the six existing lists as plain
  arrays. Paginating those lists would break every one of them, and the brief
  adds one endpoint; nothing else changes.

  PASS if no REQUIREMENTS entry makes re-paginating, re-shaping or versioning
  the six existing list endpoints a non-negotiable of this change. The gap
  may be named in RISKS, as a later migration, or as advice for a future
  change: that passes.
  FAIL if REQUIREMENTS demands that the existing lists be paginated or
  changed as part of this change, or requires a new API version for the
  whole API because of the new endpoint.
weight: 1
---

Keeps the six existing lists out of this change's REQUIREMENTS: consistency
is restored by a named follow-up, not by breaking their five callers now.
