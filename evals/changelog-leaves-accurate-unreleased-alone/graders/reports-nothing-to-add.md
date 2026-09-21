---
type: llm
focus: last_message
criteria: |
  PASS if the report states plainly that nothing was added to the changelog
  because `[Unreleased]` already covers the user-facing commits since the
  last tag — an explicit "no change" outcome.
  FAIL if the report claims to have added, updated, or reorganised entries,
  or is vague enough that a reader cannot tell whether the file changed.
weight: 1
---

Says out loud that it changed nothing, so a caller can tell the difference
between "already up to date" and "ran and did nothing useful".
