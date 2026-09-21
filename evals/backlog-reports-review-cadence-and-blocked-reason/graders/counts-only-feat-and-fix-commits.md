---
type: llm
focus: last_message
criteria: |
  Nine commits landed after the hash recorded in `.vibe/last-review.md`:
  six with a `feat:` or `fix:` prefix, and three with a `chore:` prefix.

  PASS if the report states that 6 changes (feat:/fix: commits) landed since
  the recorded review — the number 6, however it is worded.
  FAIL if it reports 9, or any other count, or gives no count at all.
weight: 2
---

Counts the 6 `feat:`/`fix:` commits since the recorded review hash and ignores the 3 `chore:` commits.

