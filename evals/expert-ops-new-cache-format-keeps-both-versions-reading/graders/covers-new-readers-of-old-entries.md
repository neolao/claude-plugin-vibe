---
type: llm
focus: last_message
criteria: |
  Entries written before the rollout are bare number strings that live for
  24 hours: a pod on the new version reads `price:<sku>` and finds "19.90"
  where it expects a structured entry, for up to a day after its own
  deploy.

  PASS if REQUIREMENTS, RISKS or TEST SCENARIOS says that the new version
  must handle the bare-number entries already in the cache — parse the old
  format as well, treat an unparseable entry as a cache miss and refetch,
  or read from a new key space the old entries never used — with a stated
  behaviour or a test scenario for a new pod meeting an old entry.
  FAIL if the reply never addresses the entries written before the rollout
  and what a new pod does when it reads one, or assumes the cache is empty
  or flushed at deploy without saying so as a requirement.
weight: 2
---

Requires the new version to cope with the bare-number entries that live in
the cache for a day after the rollout: compatibility runs in both
directions.
