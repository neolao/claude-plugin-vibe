---
type: llm
focus: last_message
criteria: |
  The repository is tagged v1.2.0, and a later commit carries the tags
  deploy-2026-10-30 and vnext.
  PASS if the report says the commits were taken since v1.2.0 (or "since
  the last version tag, v1.2.0"), whether or not it mentions the other
  tags.
  FAIL if the report names vnext or deploy-2026-10-30 as the tag the
  range starts at, or says no tag was found.
weight: 1
---

The caller can tell which tag scoped the range.
