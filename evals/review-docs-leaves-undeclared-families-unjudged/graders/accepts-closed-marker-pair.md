---
type: llm
focus: last_message
criteria: |
  fixtures/README.md holds its documentation list between
  `<!-- vibe:begin:docs-index -->` and `<!-- vibe:end:docs-index -->`,
  both present, and the three pages listed exist.

  PASS if no `high` or `medium` severity finding names the docs-index
  markers, the managed section or the README's index as malformed,
  unclosed or drifting. A `low` finding passes, and so does a report with
  no findings at all.
  FAIL if the marker pair or the index is flagged at high or medium
  severity.
weight: 1
---

Does not report a managed-section pair that is properly closed and
lists what exists.
