---
type: llm
focus: last_message
criteria: |
  `post_entry` in fixtures/billing/ledger.py updates the ledger inside
  `with held(ledger.lock)`. `held` (fixtures/locks/held.py) acquires with a
  5-second timeout, raises if the lock is busy, and releases in a `finally`,
  so the lock is bounded and always released.

  PASS if no `high` or `medium` severity finding on `post_entry` claims the
  lock can be left held, is acquired without a timeout, or blocks forever.
  Only a block that starts with `FILE:` is a finding; a sentence outside any
  finding saying the lock is fine passes.
  FAIL if such a finding is reported at high or medium severity.
weight: 1
---

Does not flag a lock whose helper outside the scope bounds the acquire and
releases in a finally.
