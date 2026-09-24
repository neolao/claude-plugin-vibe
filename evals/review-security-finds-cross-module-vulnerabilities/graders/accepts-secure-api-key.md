---
type: llm
focus: last_message
criteria: |
  FAIL if any finding flags `tokens.api_key` or `ids.secure_id`
  (fixtures/archiver/tokens.py, fixtures/archiver/ids.py) as a weak or
  predictable token. `secure_id` uses `secrets.token_urlsafe`.
  A finding about `share_token` or `short_id` does not count against this
  grader, even if it points at `secure_id` as the fix. Neither does a
  finding about how the key is stored in the database: that is not a claim
  that the key is predictable.
  PASS otherwise, including when the report has no finding at all.
weight: 1
---

Does not flag the `secrets`-based API key as weak.
