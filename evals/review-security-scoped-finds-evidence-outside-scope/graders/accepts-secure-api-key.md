---
type: llm
focus: last_message
criteria: |
  FAIL if any finding flags `ids.secure_id` (fixtures/archiver/lib/ids.py)
  or `tokens.api_key` as a weak or predictable token: `secure_id` uses
  `secrets.token_urlsafe`. A finding about `short_id` or `share_token`
  does not count against this grader, even if it points at `secure_id` as
  the fix.
  PASS otherwise, including when the report has no finding at all.
weight: 1
---

Does not flag the `secrets`-based id as weak.
