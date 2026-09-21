---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS or RISKS calls out that the payment provider can
  redeliver the same webhook event more than once, and ties this to the
  rule that retries/reprocessing must only happen around an idempotent
  write into the `events` table (e.g. dedupe by event id, upsert instead
  of insert) — not a generic "add retries with backoff" statement that
  ignores the duplicate-delivery detail from the brief.
  FAIL if duplicate delivery / idempotent processing is not addressed, or
  only generic retry advice is given without the idempotency angle.
weight: 2
---

Ties retry/reprocessing behavior to the provider's documented at-least-once
delivery and the need for idempotent writes.
