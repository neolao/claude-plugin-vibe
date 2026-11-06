---
type: llm
focus: last_message
criteria: |
  The brief describes a six-year-old schema whose forty tables share one
  style: `bigserial` integer ids, snake_case plural names, `created_at` and
  `updated_at` as `timestamptz`, a nullable `archived_at` on every table in
  place of deleting rows, and numbered SQL files run by Flyway. The expert's
  own checklist says the schema's existing conventions beat its defaults,
  even where it would pick otherwise.

  PASS if REQUIREMENTS requires the new `comments` table to reuse the
  existing conventions — at least the integer id, the `archived_at`
  column (or the existing archive pattern by name) and the Flyway SQL
  migration file — and prescribes no different style for it.
  FAIL if any REQUIREMENTS entry prescribes, for the new table, a style that
  differs from the existing one: a UUID or ULID key, a `deleted`/`is_deleted`
  flag or a hard delete in place of `archived_at`, camelCase or singular
  naming, a `timestamp without time zone`, or a migration written for a
  different tool (an ORM's migration class, a hand-run script). A different
  style suggested only in RISKS as a gap or a later migration still passes.
weight: 2
---

Requires the new table to reuse the schema's id type, archive pattern,
naming and migration tool, instead of prescribing the checklist's own
defaults as a second style.
