---
type: llm
focus: last_message
criteria: |
  The repository is tagged v1.2.0 and, on a later commit, v1.3.0-rc.1;
  there is no v1.3.0 tag.
  PASS if the report says the commits were taken since v1.3.0-rc.1 (or
  "since the last version tag, v1.3.0-rc.1").
  FAIL if the report names v1.2.0 as the tag the range starts at, or
  says no tag was found.
weight: 1
---

The caller can tell which tag scoped the range.
