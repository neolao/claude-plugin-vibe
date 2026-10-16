---
type: llm
focus: last_message
criteria: |
  The repository has no tag.
  PASS if the report says that no tag was found and that the history was
  read from its start (or from the release commit), and that the commits
  already covered by the released section were skipped.
  FAIL if the report claims a tag was used, or says nothing about why the
  CSV export and pagination commits produced no entry.
weight: 1
---

The caller can tell a deliberate skip from a missed commit.
