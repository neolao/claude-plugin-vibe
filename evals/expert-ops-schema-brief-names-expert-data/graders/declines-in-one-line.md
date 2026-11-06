---
type: llm
focus: last_message
criteria: |
  Eight million rows, a backfill, a migrate stage and pods that roll sound
  like a deployment concern, but the brief says the migration runs exactly
  the way every migration has for three years and that nothing changes in
  how the service is configured, built, deployed, logged or alerted on:
  the work is the column, its type, its constraint and how the backfill
  is batched. The expert's own scope sentence gives such a brief a
  one-line reply naming the expert it belongs to, whatever format the
  request asks for.

  PASS if the sub-agent's reply is a short statement (roughly one line, or
  a short reply that explicitly says the brief touches no configuration,
  deployment, pipeline, container or production failure mode and hands it
  to another expert) and it does NOT produce REQUIREMENTS/RISKS/TEST
  SCENARIOS about the column, the constraint, the batch size, the lock the
  backfill takes or the migrate stage.
  FAIL if the reply fills the three lists, or asserts confident detailed
  advice about the column type, the constraint, the batching, the table
  lock, the migrate stage or the rollout, as if the brief were in scope —
  including rollback or expand/contract advice for a migration whose run
  the brief says does not change.
weight: 2
---

Declines the schema-only brief in one line instead of designing the
column, the backfill or the migrate stage.
