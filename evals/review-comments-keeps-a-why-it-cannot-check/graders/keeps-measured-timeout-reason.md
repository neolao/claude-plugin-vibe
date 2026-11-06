---
type: llm
focus: last_message
criteria: |
  fixtures/exporter/client.py reads `TIMEOUT = 8  # seconds: the partner's
  p99 measured at 6.2 s over October 2026`. The unit is not in the name, and
  no file in the repository can confirm or deny the measurement.

  PASS if no `high` or `medium` severity finding calls that comment
  misleading or redundant, and no finding at any severity asks to delete it
  or to drop the measurement. A `low` finding that only shortens its
  wording passes, as does a report with no findings at all.
  FAIL if the comment is flagged at high or medium severity as Misleading
  or Redundant (or equivalent), or if a finding suggests deleting it or
  removing the p99 figure.
weight: 1
---

Keeps a unit plus a measurement the repository cannot check: there is
nothing to compare the figure against, so it is not Misleading, and the
unit alone makes the comment useful.
