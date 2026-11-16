---
type: llm
focus: last_message
criteria: |
  The brief describes an API whose fourteen endpoints share one style for
  three years: `?page=`/`?pageSize=` pagination with `data` and
  `meta.totalCount`, camelCase fields, an `{ "error": { "code", "message" } }`
  envelope, resources nested under the account. Partners generated their
  clients from it. The expert's own checklist says the API's existing
  conventions beat its defaults, even where it would pick otherwise.

  PASS if REQUIREMENTS requires the two new endpoints to reuse the existing
  conventions — at least the existing pagination parameters and response
  shape for the comment list, and the existing error envelope or casing —
  and prescribes no different style for them.
  FAIL if any REQUIREMENTS entry prescribes, for the new endpoints, a style
  that differs from the existing one: cursor or keyset pagination in place
  of `?page=`/`?pageSize=`, snake_case or kebab-case fields, a different
  error envelope (RFC 7807 problem details, a top-level `errors` array), or
  a flatter URL outside the account nesting. A different style suggested
  only in RISKS as a gap or a later migration still passes.

  Only an entry that replaces one of these four named conventions counts
  against the reply. Something the brief gives no convention for — a sort
  parameter, an idempotency header, a page-size maximum, a validation rule
  or a status code — is an addition, not a second style, and still passes.
weight: 2
---

Requires the new endpoints to reuse the API's existing pagination, casing,
error envelope and nesting, instead of prescribing the checklist's own
defaults as a second style.
