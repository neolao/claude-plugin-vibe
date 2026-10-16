---
type: llm
focus: last_message
criteria: |
  Four commits since the tag: a `wip:` that started a PDF export and was
  never finished, a `refactor:` from a review, a `test:`, and a `fix:`.
  PASS if the report says the wip (and the refactor and test) commits were
  discarded or skipped as noise, and does not claim that a PDF export was
  added to the changelog.
  FAIL if the report says a PDF export entry was added, or gives no account
  of what was discarded.
weight: 1
---

The report must make the discard visible, so the caller can tell a
skipped wip from a missed feature.
