---
type: llm
focus: last_message
criteria: |
  `short_id` in fixtures/archiver/lib/ids.py draws from `random.choices`.
  Its only caller, `restore` in fixtures/archiver/commands.py (outside the
  scope), uses it as the job reference printed to the operator; the share
  token and the API key in fixtures/archiver/tokens.py both come from
  `secure_id`, which uses `secrets.token_urlsafe`.

  PASS if no `high` or `medium` severity `Crypto` (or clearly equivalent
  category name) finding targets `short_id` or `random`. A `low` finding
  passes, and so does a report with no findings at all.
  FAIL if `short_id` is reported as a weak or predictable security token
  at high or medium severity.
weight: 1
---

Does not call a random id a weak token when its only use, outside the
scope, is a label.
