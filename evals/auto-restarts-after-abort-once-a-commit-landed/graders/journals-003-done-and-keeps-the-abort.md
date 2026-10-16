---
type: llm
focus: { source: file, path: ".vibe/auto-state.md" }
criteria: |
  The file held one run section whose only line recorded 003 as aborted on a
  broken build. A new run then shipped 003.

  PASS if the file now holds two run sections, the earlier one still carrying
  the aborted line for 003, and the later one recording 003 with a `done`
  verdict (and a commit hash or equivalent reference).
  FAIL if the earlier section or its aborted line was removed or rewritten,
  if 003 is recorded as blocked or aborted in the new section, or if there is
  no new section at all.
weight: 2
---

The new run is journaled in its own section; history is kept.
