---
type: llm
focus: last_message
criteria: |
  PASS if the reply states a rollback path and addresses that structured
  entries may already sit in the cache (for up to 24 hours) when the
  rollback happens: the rolled-back version still reads a price (the old
  key kept bare, entries under a new key space the old version ignores, a
  tolerant reader, or the affected keys deleted as part of the rollback).
  FAIL if there is no rollback path, or the rollback is "redeploy the
  previous version" with no word on the new-format entries already written.
weight: 1
---

States a rollback path that holds while new-format entries are still in the
cache.
