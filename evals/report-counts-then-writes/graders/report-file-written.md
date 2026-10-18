---
type: llm
focus: trace
criteria: |
  PASS if the trace shows a Bash call to the skill's `report.sh` with the
  `write` operation whose output is a path matching
  `.vibe/reports/<timestamp>-feature.md`, and the final message quotes that
  path after a `📊 Report —` marker.
  FAIL if no `write` call was made, if the report was written by hand
  (Write tool) instead of through the script, or if the path is elsewhere
  than `.vibe/reports/`.
weight: 2
---

The report exists, under `.vibe/reports/`, produced by the script and not
hand-written.
