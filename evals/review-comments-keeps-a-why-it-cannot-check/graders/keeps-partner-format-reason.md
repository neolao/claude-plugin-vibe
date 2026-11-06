---
type: llm
focus: last_message
criteria: |
  fixtures/exporter/payload.py reads `stamp = now.strftime("%Y%m%dT%H%M%SZ")
  # ISO 8601 basic form: the partner rejects the extended one`. The format
  string shows the basic form; that the partner rejects the extended form
  is external and unverifiable from the repository.

  PASS if no `high` or `medium` severity finding calls that comment
  misleading or redundant, and no finding at any severity asks to delete
  it. A `low` finding that only shortens its wording passes, as does a
  report with no findings at all.
  FAIL if the comment is flagged at high or medium severity as Misleading
  or Redundant (or equivalent), or if a finding suggests deleting it.
weight: 1
---

Keeps the reason for choosing a format the code merely applies: the
partner's constraint lives outside the repository.
